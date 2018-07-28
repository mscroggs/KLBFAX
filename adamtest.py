from helpers import url_handler
code = "940GZZLUBST"
tube_times = url_handler.load_json("http://api.tfl.gov.uk/stopPoint/"+code+"/arrivals?mode=tube")
tubes = []
platforms = []
for b in tube_times:
    p = b['platformName'];
    if p not in platforms:
        platforms.append(p)
    tubes.append((b['platformName'],int(b['timeToStation']),str(b['timeToStation']//60).rjust(2,' ')+" min",b['lineName'].replace('Hammersmith','Ham').replace('Waterloo','Wloo'),b['towards'],b['currentLocation']))
tubes.sort()

#platforms = sorted(platforms, key=lambda x: int(x[-2:]));
num_platforms = len(platforms);
max_tubes_per_platform = 23//num_platforms-2;

tubes_per_platform = [[] for i in xrange(len(platforms))]
lines_per_platform = [[] for i in xrange(len(platforms))]

for pnum, platform in enumerate(platforms):
    for tube in tubes:
        if tube[0] == platform:
            tubes_per_platform[pnum].append(tube)
            line = tube[3]
            if line not in lines_per_platform[pnum]:
                lines_per_platform[pnum].append(line)

#for platform in lines_per_platform:
#    platform.sort()

platform_order = sorted(range(len(platforms)), key=lambda k: lines_per_platform[k][0] + " " + platforms[k])

for pnum in platform_order:
    platform = platforms[pnum]
    print " ".join(sorted(lines_per_platform[pnum])) + " " + platform
    for t in tubes_per_platform[pnum][:max_tubes_per_platform]:
        print t[2] + ' ' + t[3] + ' ' + t[4] + ' ' + t[5].replace("Platform ","P")
        #print "\n"
