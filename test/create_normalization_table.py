import os

###All normalizations are provided to 1fb-1 of lumi in these tables

dir_input = "crab_projects/samples/"
list_dirs = os.listdir(dir_input)

if not os.path.exists("rootfiles"):
    os.makedirs("rootfiles")

output_filename = "rootfiles/Normalizations_table.txt"

##These are in pb
def get_xsec_fromsample(samplename):
    
    if samplename == "ttbar":
        return 831.76

    if samplename == "DY_5_50":
        return 71310.0

    if samplename == "DY_50":
        return 6225.2

    if samplename == "QCD_15_30":
        return 1837410000.0

    if samplename == "QCD_30_50":
        return 140932000.0

    if samplename == "QCD_50_80":
        return 19204300.0

    if samplename == "QCD_80_120":
        return 2762530.0

    if samplename == "QCD_120_170":
        return 471100.0

    if samplename == "QCD_170_300":
        return 117276.0

    if samplename == "QCD_300_470":
        return 7823.0

    if samplename == "QCD_470_600":
        return 648.2

    if samplename == "QCD_600_800":
        return 186.9

    if samplename == "QCD_800_1000":
        return 32.293

    if samplename == "QCD_1000_1400":
        return 9.4183

    if samplename == "QCD_1400_1800":
        return 0.84265

    if samplename == "QCD_1800_2400":
        return 0.114943

    if samplename == "SingleTop_tW":
        return 35.6

    if samplename == "SingleAntiTop_tW":
        return 35.6

    if samplename == "ZZ":
        return 16.523

    if samplename == "WW":
        return 63.21

    if samplename == "WZ":
        return 47.13

    if samplename == "WJetsToLNu":
        return 61526.7

    if samplename == "Signal_H500_A200":
        return 1.96

    if samplename == "Signal_H700_A200":
        return 0.22

    if samplename == "Signal_H800_A300":
        return 0.10

##Now starts the program

out_file = open(output_filename,"w")


for dirname in list_dirs:
    samplename = dirname.split("crab_HAA4bAnalysis_")[1]
    print "Processing sample dir " + dirname
    crab_command = "crab report -d " + dir_input + dirname + " | grep read"
    if samplename == "QCD_15_30":
        number_events = 38425945.*186./187.
        print "No. of events to be processed = " + str (number_events) + "\n"
    #elif samplename == "WJetsToLNu":
    #    number_events = 72207128.0
    else :
        event_string = os.popen(crab_command).read()
        #number_events = float((event_string.split())[0])
        number_events = float((event_string.split())[4])
        print "No. of events to be processed = " + str (number_events) + "\n"
    #xsection = float(get_xsec_fromsample(samplename))
    xsection = get_xsec_fromsample(samplename)  
    scale_factor = float(xsection*1000./number_events)
    write_string = samplename + " " + str(scale_factor) + "\n"
    out_file.write(write_string)

out_file.close()
