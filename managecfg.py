def process_file(nb_classes, width, height,filename,learning_rate):
    lines = []
    filetxt = open(filename,"r")
    for line in filetxt:
        lines.append(line)
    filetxt.close()
    index=0
    for line in lines:
        if "width" in line:
            if not "#" in line:
                lines[index] = "width = " + str(width)
        if "height" in line:
            if not "#" in line:
                lines[index] = "height = " + str(height)
        if "filters = 255" in line or "filters=255" in line:
            if not "#" in line:
                lines[index] = "filters = " + str((nb_classes+5)*3)
                print("filters = " + str((nb_classes+5)*3))
        if "classes" in line:
            if not "#" in line:
                lines[index] = "classes = " + str(nb_classes)
        if "batch" in line:
            if not "#" in line:
                lines[index] = "batch = " + str(64)
        if "subdivisions" in line:
            if not "#" in line:
                lines[index] = "subdivisions = " + str(16)
        if "max_batches" in line:
            if not "#" in line:
                lines[index] = "max_batches = " + str(nb_classes*2000)
        if "learning_rate" in line:
            if not "#" in line:
                lines[index] = "learning_rate = " + str(learning_rate)
        if "steps" in line:
            if not "#" in line:
                lines[index] = "steps=" + str(int((nb_classes*2000)*80/100)) + "," + str(int((nb_classes*2000)*90/100))
                print("steps=" + str(int((nb_classes*2000)*80/100)) + "," + str(int((nb_classes*2000)*90/100)))
        index += 1
    file = open(filename,"w")
    for line in lines:
        if line != "\n":
            if "\n" in line:
                line = line.replace("\n","")
                file.write(str(line) + "\n")
            else:
                file.write(str(line) + "\n")
    file.close()

