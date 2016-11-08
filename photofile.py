from subprocess import call
photofile = "/home/pi/Dropbox- Uploader/dropbox_uploader.sh upload /home/pi/photo0001.jpg photo00001.jpg"
call ([photofile], shell=True)
