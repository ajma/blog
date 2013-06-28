Find Used Memory Slots via Command Line
#######################################
:date: 2012-01-14
:tags: windows,config,ram,memory
:category: Windows

Yesterday, I was going to order some more ram for my laptop and I didn’t have a  screwdriver around to check if the 4gb in my current setup was composed of one 4gb dimm or 2 x 2gb dimm. I found a nifty command-line options (Windows only) to display this information for me.

wmic MEMORYCHIP get banklabel, capacity, caption, devicelocator, partnumber


via `Find Used Memory Slots via Command Line <http://support.risualblogs.com/blog/2010/05/04/find-used-memory-slots-via-command-line/>`_
