from PIL import Image
import numpy as np
import glob, os
for f in sorted(glob.glob(r'D:/2/tmp_unity_scene/menu_*.png')):
    im = Image.open(f).convert('RGB')
    a = np.asarray(im)
    m = a.mean(axis=2)
    uniq = len(np.unique(a.reshape(-1, 3)[::37], axis=0))
    print(os.path.basename(f)[:58], 'mean=%.1f' % m.mean(), 'dark=%.3f' % (m < 8).mean(), 'colors~', uniq)
