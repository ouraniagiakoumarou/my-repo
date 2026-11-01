def CE(floors[], inside[], waiting pickup, destination, floorNum, capacity, calledElevators[], directions[]):

    best = 0 #kalytero asanser
    maxScore = -1

    #pou theloun na pane
    if destination > pickup:
        direction = 'UP'
    elif destination < pickup:
        direction = 'DOWN'
    else:
        direction = 'ERROR'

    #gia kathe apo ta 3 asanser
    for i in range (3):
        fit = false #an xvrane sto sygkekrimeno asanser
        if inside[i] + waiting > capacity:
            fit = true
        
        #diafora orofwn
        distance = floors[i] - pickup
        distance = abs(distance)
        directionX = directions[i] #pou thelei na paei to asanser

        #briskw arxiko score(1000-Apostash orofwn)
        float y = (distance * 100)/ floorNum #%apostashs se sxesh me oloys toys orofous
        score = (1000-y)

        #afairw pontous analoga me ta atoma
        float x = (inside*100)/capacity #%pou einai gemato
        if x == 100:
            score = 0
        else:
            score -=x

        #afairw analoga me kateythinsi
        if direction == 'DOWN' and floors[i] < pickup:
            score+=50
        elif direction == 'UP' and floors[i] > pickup:
            score+=50 #+50 giati pane sthn idia kateythinsi

        #teliko score
        if score > maxScore:
            maxScore = Score
            best = i+1

        #prosthikh sthn DYNAMIC lista gia na exoume tis amesos epomenes kalyteres epiloges
        if best not in calledElevators:
            calledElevators += best
    
    return best

    