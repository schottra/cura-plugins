#Name: PerExtruderESteps
#Info: Allows you to set different steps/mm values for each extruder
#Help: PerExtruderESteps
#Depend: GCode
#Type: postprocess
#Param: eSteps0(float:0) Steps/mm for extruder 0
#Param: eSteps1(float:0) Steps/mm for extruder 1
#Param: eSteps2(float:0) Steps/mm for extruder 2


step_values = [eSteps0, eSteps1, eSteps2]

with open(filename, "r") as f:
    lines = f.readlines()


with open(filename, "w") as f:
    for line in lines:
        f.write(line)
        if line[0] == 'T':
            extruder_index = int(line[1])
            step_value = step_values[extruder_index]
            f.write("M92 E%f" % float(step_value))


