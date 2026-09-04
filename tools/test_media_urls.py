import urllib.request

test_images = [
    ('Hero Logo', 'https://static.wixstatic.com/media/14e118_4bf7379891324d5b958fc95e6f706967~mv2.png'),
    ('About Us Bg/Img', 'https://static.wixstatic.com/media/14e118_7dccd812a3af43a886ed3669e43263d8~mv2.jpg'),
    ('Portfolio Banner', 'https://static.wixstatic.com/media/14e118_7cfb2596ba78440585ef5b8a6e09add6~mv2.jpg'),
    ('Team Pic', 'https://static.wixstatic.com/media/14e118_943ecf4b0db94611a6baff1f6e69c3d3~mv2.jpg'),
    ('Silvario Marzin', 'https://static.wixstatic.com/media/14e118_00f969ab64cf45e290fc0c24a78bfbab~mv2.jpg'),
    ('Footer Logo', 'https://static.wixstatic.com/media/14e118_cf382f8f9e5b44cd9a9084c78f9a24ff~mv2.png'),
    ('Blueprint Icon', 'https://static.wixstatic.com/media/14e118_f44b0ddb3c9a4bec8f52cc7de4606798~mv2.png'),
    ('House Icon', 'https://static.wixstatic.com/media/11062b_bf349604256e48abaf8a452aefe9436d~mv2.png'),
    ('Contract Icon', 'https://static.wixstatic.com/media/14e118_ed96042c89b3400a93ed20f56c58c7e7~mv2.png'),
    ('Hero Poster', 'https://static.wixstatic.com/media/11062b_4f14b356c1df4854968cf1cc94ca98c5f000.jpg'),
]

print("Testing direct downloads:")
for name, url in test_images:
    req = urllib.request.Request(url, method='HEAD')
    res = urllib.request.urlopen(req)
    cl = res.headers.get('Content-Length', '0')
    print(f"[{res.status}] {name}: {int(cl)/1024:.1f} KB -> {url.split('/')[-1]}")
