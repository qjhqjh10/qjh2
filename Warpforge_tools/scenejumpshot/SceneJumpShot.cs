using System;
using System.Collections;
using System.IO;
using System.Text;
using MelonLoader;
using UnityEngine;
using UnityEngine.SceneManagement;

[assembly: MelonInfo(typeof(SceneJumpShot.SceneJumpMod), "SceneJumpShot", "3.1.0", "CC")]
[assembly: MelonGame("Everguild", "Warpforge")]

namespace SceneJumpShot
{
    public class SceneJumpMod : MelonMod
    {
        private const string BundlePathSuffix = "aa/StandaloneWindows64";
        private const string CfgPath = "d:/2/unity_run_ref/UserData/sjs_dump_cfg.txt";

        public override void OnInitializeMelon()
        {
            LoggerInstance.Msg("[SJS] v3.1 runtime UI dumper loaded");
            MelonCoroutines.Start(Boot());
        }

        private string Esc(string s)
        {
            return (s ?? "").Replace("\t", " ").Replace("\n", "\\n").Replace("\r", "");
        }

        private void DumpGo(Transform t, string path, StreamWriter w)
        {
            var go = t.gameObject;
            var sb = new StringBuilder();
            sb.Append(path).Append('\t').Append(Esc(go.name))
              .Append('\t').Append(go.activeSelf).Append('\t').Append(go.activeInHierarchy);
            try
            {
                var rt = go.GetComponent<RectTransform>();
                if (rt != null)
                {
                    var ap = rt.anchoredPosition; var sd = rt.sizeDelta;
                    var amin = rt.anchorMin; var amax = rt.anchorMax; var pv = rt.pivot;
                    sb.Append("\tRT\t").Append(ap.x.ToString("F1")).Append(',').Append(ap.y.ToString("F1"))
                      .Append('\t').Append(sd.x.ToString("F1")).Append(',').Append(sd.y.ToString("F1"))
                      .Append('\t').Append(amin.x.ToString("F3")).Append(',').Append(amin.y.ToString("F3"))
                      .Append('\t').Append(amax.x.ToString("F3")).Append(',').Append(amax.y.ToString("F3"))
                      .Append('\t').Append(pv.x.ToString("F3")).Append(',').Append(pv.y.ToString("F3"));
                }
                else
                {
                    sb.Append("\tTF\t\t\t\t\t");
                }
            }
            catch { sb.Append("\tRT?\t\t\t\t\t"); }

            try
            {
                // TMP 程序集在 cpp2il 下编译引用不可见 → 运行时反射 (2026-08-25)
                object comp = null;
                try
                {
                    var tmpT = Il2CppSystem.Type.GetType("TMPro.TextMeshProUGUI, Unity.TextMeshPro");
                    comp = tmpT != null ? go.GetComponent(tmpT) : null;
                }
                catch { comp = null; }
                if (comp != null)
                {
                    var st = comp.GetType();
                    var txtF = st.GetField("m_text");
                    var fsF = st.GetField("m_fontSize");
                    string txt = txtF != null ? (txtF.GetValue(comp) ?? "").ToString() : "";
                    object fso = fsF != null ? fsF.GetValue(comp) : null;
                    float fsv = 0f; float.TryParse((fso ?? "0").ToString(), out fsv);
                    sb.Append("	TXT	").Append(Esc(txt)).Append('	').Append(fsv.ToString("F1"));
                }
                else
                {
                    sb.Append("			");
                }
            }
            catch { sb.Append("	TXT?		"); }

            try
            {
                var img = go.GetComponent<UnityEngine.UI.Image>();
                if (img != null)
                {
                    string sn = "";
                    try { sn = img.sprite != null ? img.sprite.name : ""; } catch { }
                    sb.Append("\tIMG\t").Append(Esc(sn));
                }
                else
                {
                    sb.Append("\t\t");
                }
            }
            catch { sb.Append("\tIMG?\t"); }

            w.WriteLine(sb.ToString());
            for (int i = 0; i < t.childCount; i++)
            {
                DumpGo(t.GetChild(i), path + "/" + go.name, w);
            }
        }

        private void DumpTree(string sceneName, string outPath)
        {
            try
            {
                using (var w = new StreamWriter(outPath, false, new UTF8Encoding(true)))
                {
                    w.WriteLine("path\tname\tactiveSelf\tactiveInHierarchy\trect\tpos\tpivot\ttext\tfontSize\tcolor\timage");
                    var scene = SceneManager.GetActiveScene();
                    GameObject[] roots = scene.GetRootGameObjects();
                    foreach (var go in roots)
                    {
                        DumpGo(go.transform, go.name, w);
                    }
                }
                LoggerInstance.Msg("[SJS] DUMP " + sceneName + " -> " + outPath + " (" + (new FileInfo(outPath)).Length + " bytes)");
            }
            catch (Exception e)
            {
                LoggerInstance.Msg("[SJS] dump fail: " + e);
            }
        }

        // RT+ReadPixels 截图（ScreenCapture 在 interop 崩，2026-08-25 已验证此路）
        private void CaptureShot(string path, int w = 1920, int h = 1080)
        {
            try
            {
                Camera cam = Camera.main;
                if (cam == null)
                {
                    var cams = Camera.allCameras;
                    if (cams != null && cams.Length > 0) cam = cams[0];
                }
                if (cam == null) { LoggerInstance.Msg("[SJS] shot fail: no camera"); return; }
                var rt = new RenderTexture(w, h, 24);
                var prev = cam.targetTexture;
                cam.targetTexture = rt;
                cam.Render();
                RenderTexture.active = rt;
                var tex = new Texture2D(w, h, TextureFormat.RGB24, false);
                tex.ReadPixels(new Rect(0, 0, w, h), 0, 0);
                tex.Apply();
                File.WriteAllBytes(path, tex.EncodeToPNG());
                cam.targetTexture = prev;
                RenderTexture.active = prev;
                UnityEngine.Object.Destroy(tex);
                UnityEngine.Object.Destroy(rt);
                LoggerInstance.Msg("[SJS] SHOT " + path);
            }
            catch (Exception e) { LoggerInstance.Msg("[SJS] shot fail: " + e); }
        }

        // ---------- BattleDrive v3.2 (2026-08-25): 用战斗场景自带 Debug 按钮给双方发牌/加能量, 抓实战手牌 ----------
        private Transform FindGo(Transform t, string name)
        {
            if (t.name == name) return t;
            for (int i = 0; i < t.childCount; i++)
            {
                var r = FindGo(t.GetChild(i), name);
                if (r != null) return r;
            }
            return null;
        }

        private bool Click(Transform root, string goName, int reps = 1)
        {
            var go = FindGo(root, goName);
            if (go == null) { LoggerInstance.Msg("[SJS] drive: not found " + goName); return false; }
            var btn = go.GetComponent<UnityEngine.UI.Button>();
            if (btn == null) { LoggerInstance.Msg("[SJS] drive: no Button on " + goName); return false; }
            for (int i = 0; i < reps; i++) btn.onClick.Invoke();
            LoggerInstance.Msg("[SJS] drive: clicked " + goName + " x" + reps);
            return true;
        }

        // v3.5: 编译期引用游戏程序集 (MelonLoader/Il2CppAssemblies/Assembly-CSharp.dll)
        private void InitBattleManager()
        {
            try
            {
                var bm = FindGo(SceneManager.GetActiveScene().GetRootGameObjects()[0].transform, "BattleManager");
                foreach (var ro in SceneManager.GetActiveScene().GetRootGameObjects())
                {
                    bm = FindGo(ro.transform, "BattleManager");
                    if (bm != null) break;
                }
                if (bm == null) { LoggerInstance.Msg("[SJS] init: no BattleManager GO"); return; }
                var comp = bm.GetComponent<BattleManager>();
                if (comp == null) { LoggerInstance.Msg("[SJS] init: no BattleManager component"); return; }
                LoggerInstance.Msg("[SJS] init: BattleManager component OK");
                try { comp.Initialize(); LoggerInstance.Msg("[SJS] init: Initialize() ok"); }
                catch (Exception e) { LoggerInstance.Msg("[SJS] init Initialize err: " + e.Message); }
                // 私有方法走反射 (编译期类型下方法列表真实可见)
                foreach (var mname in new[] { "SetupTestButtons", "SetupInitialState", "StartBattleManager" })
                {
                    try
                    {
                        var mi = comp.GetType().GetMethod(mname,
                            System.Reflection.BindingFlags.Public | System.Reflection.BindingFlags.NonPublic |
                            System.Reflection.BindingFlags.Instance);
                        if (mi != null) { mi.Invoke(comp, null); LoggerInstance.Msg("[SJS] init: invoked " + mname); }
                        else LoggerInstance.Msg("[SJS] init: no method " + mname);
                    }
                    catch (Exception e) { LoggerInstance.Msg("[SJS] init " + mname + " err: " + e.Message); }
                }
            }
            catch (Exception e) { LoggerInstance.Msg("[SJS] init fail: " + e); }
        }

        private IEnumerator BattleDrive()
        {
            Transform bp = null;
            foreach (var ro in SceneManager.GetActiveScene().GetRootGameObjects())
            {
                bp = FindGo(ro.transform, "DebugButtons");
                if (bp != null) break;
            }
            if (bp == null)
            {
                LoggerInstance.Msg("[SJS] drive FAIL: no DebugButtons in any root");
                yield break;
            }
            InitBattleManager();
            yield return new WaitForSecondsRealtime(1f);
            bp.gameObject.SetActive(true);
            LoggerInstance.Msg("[SJS] drive: DebugButtons activated");
            yield return new WaitForSecondsRealtime(1f);

            // 卡选择器 (Card Picker = 下拉框): 用反射设 value → 后续 AddSelectedCardButton 用
            var picker = FindGo(bp, "Card Picker");
            if (picker != null)
            {
                try
                {
                    var ddT = Il2CppSystem.Type.GetType("TMPro.TMP_Dropdown, Unity.TextMeshPro");
                    if (ddT != null)
                    {
                        var dd = picker.GetComponent(ddT);
                        if (dd != null)
                        {
                            var valP = dd.GetType().GetProperty("value");
                            if (valP != null) { valP.SetValue(dd, 2); LoggerInstance.Msg("[SJS] drive: picker value=2"); }
                        }
                    }
                }
                catch (Exception e) { LoggerInstance.Msg("[SJS] drive picker fail: " + e); }
            }
            else LoggerInstance.Msg("[SJS] drive: no Card Picker node");

            // 玩家: 加能量+发牌; 敌方: 发牌
            Click(bp, "AddMana", 3);
            yield return new WaitForSecondsRealtime(0.5f);
            Click(bp, "AddPlayerCardButton", 4);
            yield return new WaitForSecondsRealtime(1f);
            Click(bp, "AddSelectedCardButton", 1);
            yield return new WaitForSecondsRealtime(1f);
            Click(bp, "AddCardButton", 2);   // 敌方发牌
            yield return new WaitForSecondsRealtime(4f);   // 等布局/飞行动画
            LoggerInstance.Msg("[SJS] drive sequence done");
        }

        private IEnumerator Boot()
        {
            yield return new WaitForSecondsRealtime(10f);
            string bundleName = "";
            float wait = 12f;
            string outDir = "D:/2/Unity参照管线_0825/data";
            string multi = ""; // 检查点列表,逗号分隔秒数, v3.1 多点头
            try
            {
                if (File.Exists(CfgPath))
                {
                    string[] lines = File.ReadAllLines(CfgPath);
                    if (lines.Length > 0) bundleName = lines[0].Trim();
                    if (lines.Length > 1) wait = float.Parse(lines[1].Trim());
                    if (lines.Length > 2) outDir = lines[2].Trim();
                    if (lines.Length > 3) multi = lines[3].Trim();
                }
            }
            catch (Exception e) { LoggerInstance.Msg("[SJS] cfg fail: " + e); }
            LoggerInstance.Msg("[SJS] cfg: bundle='" + bundleName + "' wait=" + wait + " out=" + outDir + " multi=" + multi);

            if (bundleName != "")
            {
                string aaDir = Application.streamingAssetsPath + "/" + BundlePathSuffix;
                AssetBundle ab = null;
                try
                {
                    foreach (var f in Directory.GetFiles(aaDir, "*.bundle"))
                    {
                        var b = AssetBundle.LoadFromFile(f);
                        if (b != null && System.IO.Path.GetFileName(f) == bundleName) ab = b;
                    }
                }
                catch (Exception e) { LoggerInstance.Msg("[SJS] bundle fail: " + e); }
                if (ab != null)
                {
                    string[] paths = ab.GetAllScenePaths();
                    if (paths.Length > 0)
                    {
                        var loadOp = SceneManager.LoadSceneAsync(paths[0], LoadSceneMode.Single);
                        while (!loadOp.isDone) yield return new WaitForSecondsRealtime(0.5f);
                        LoggerInstance.Msg("[SJS] scene: " + SceneManager.GetActiveScene().name);
                    }
                }
            }

            yield return new WaitForSecondsRealtime(wait);
            LoggerInstance.Msg("[SJS] dump start, active scene: " + SceneManager.GetActiveScene().name);

            if (multi == "drive")
            {
                yield return BattleDrive();
                DumpTree(SceneManager.GetActiveScene().name, Path.Combine(outDir, "runtime_ui_dump_drive.tsv"));
                CaptureShot(Path.Combine(outDir, "shot_drive.png"));
                LoggerInstance.Msg("[SJS] drive done");
                yield break;
            }

            string sceneName = SceneManager.GetActiveScene().name;
            string baseOut = Path.Combine(outDir, "runtime_ui_dump_" + sceneName.Replace(' ', '_'));

            if (multi == "")
            {
                DumpTree(sceneName, baseOut + ".tsv");
                CaptureShot(Path.Combine(outDir, "shot_" + sceneName.Replace(' ', '_') + ".png"));
            }
            else
            {
                float total = 0f;
                foreach (var tok in multi.Split(','))
                {
                    float sec;
                    if (!float.TryParse(tok.Trim(), out sec)) continue;
                    if (sec > total) yield return new WaitForSecondsRealtime(sec - total);
                    total = sec;
                    sceneName = SceneManager.GetActiveScene().name;
                    string tag = "t" + ((int)sec).ToString();
                    DumpTree(sceneName, baseOut + "_" + tag + ".tsv");
                    CaptureShot(Path.Combine(outDir, "shot_" + sceneName.Replace(' ', '_') + "_" + tag + ".png"));
                }
                LoggerInstance.Msg("[SJS] multi done");
            }
        }
    }
}
