# test image set demonstrator

This repository is a test / demo repository for the work in
https://github.com/matplotlib/matplotlib/pull/25734 which is based on the
[mnt/multi_imageset](https://github.com/tacaswell/matplotlib/tree/mnt/multi_imageset)
branch of [tacaswell](https://github.com/tacaswell)'s fork of Matplotlib.

For any of this to work you must use this branch.  Get it via:

```bash
git remote add tacaswell git@github.com:tacaswell/matplotlib
git remote update
git checkout -t mnt/multi_imageset
```

or

```bash
gh pr checkout 25734
```


## operation

Run pytest with external images

```bash
MPLTESTIMAGEPATH=/tmp/test_images2  pytest
```

Run pytest to generate the external images

```bash
MPLTESTIMAGEPATH=/tmp/test_images2 MPLGENERATEBASELINE=1 pytest
```

Validate the baseline images

```bash
python manage_baseline_images.py validate plotz.tests /tmp/test_images2/
```

version rev a test image

```bash
python manage_baseline_images.py rev plotz.tests.test_basic line.svg
git add plotz/tests/image_list.txt
git commit -m "Updated the test image"
```


Add a new test image

```bash
python manage_baseline_images.py add plotz.tests.test_basic yolo.png
git add plotz/tests/image_list.txt
git commit -m "Added a test image"
```
