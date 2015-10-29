# Folder2M3U
A simple script that creates M3U playlist files based on folder trees distribution.

### Why do that?
My car has an MP3 player that scans USB drives in their own way:

* Only recognizes folders with MP3 files inside, you **can not play a folder with subfolders**.
* The **playing order of the songs** is purely alphabetical, so the song number "10" will be played before the number "2", while most of the software that plays MP3 files knows how to deal with this problem.

What was my solution? Create [M3U playlists files](https://en.wikipedia.org/wiki/M3U "M3U in Wikipedia") in each folder with the correct order.

The MP3 player of the car has two options: search by folder or search lists. With the right lists it is possible to remedy the mentioned deficits.

### Folder structure

It is expected a folder structure like the following:

```
+-- Artist Withnoalbums
|   +-- 01 Song.mp3
|   +-- 02 Song.mp3
|   +-- 03 Song.mp3
+-- Artist1
|   +-- Album1
|       +-- 01 Song.mp3
|       +-- 02 Song.mp3
|       +-- 03 Song.mp3
|   +-- Album2
|       +-- 01 Song.mp3
|       +-- 02 Song.mp3
|       +-- 03 Song.mp3
+-- Artist2
|   +-- Album1
|       +-- 01 Song.mp3
|       +-- 02 Song.mp3
|       +-- 03 Song.mp3
```

The script will create the following M3U lists:

1. Artist Withnoalbums.m3u
2. Artist1.m3u
3. Artist1 - Album1.m3u
4. Artist1 - Album2.m3u
5. Artist2 - Album1.m3u

Note that the "generic" `Artist2.m3u` list is not generated because the artist has only one album.

Of course, the order of the songs is in this lists the correct =)

### License

This software is published under the MIT License (MIT).

Copyright (c) 2015 carsevilla (https://github.com/carsevilla)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


