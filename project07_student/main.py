import tool.modelPredict as modelPredict
import tool.recorder as recorder
import tool.trainModel as train

filename = ''
if __name__ == "__main__":

    print("###############################")
    print("##                           ##")
    print("##                           ##")
    print("##       voice games         ##")
    print("##                           ##")
    print("##                           ##")
    print("###############################")
    print("")
    run = True
        
    while run :
        count = 1
        # flush_input()
        print("")
        print("1. recorder        | Record your own voice and create training data. ")
        print("2. trainModel      | Train your own voice model. ")
        print("3. modelPredict    | Connect your voice to the game. ")
        print("4. exit            | Exit the operation interface. ")
        print("")
        usr_input2 = input("Please choose which type of sound to recored : ")
        
        print("You choose ", usr_input2)

        if usr_input2 == "2" :
            filename = train.main()
        elif usr_input2 == "3":
            if filename != '':
                print('[Open first chrome dino](https://chrome-dino-game.github.io/)')
                k = input("Enter any key")
                if k != '':
                    modelPredict.main(filename)
            else:
                print('Error! You have not trained the model yet, please train a version of the model')
        elif usr_input2 == "1" :
            recorder.main()
        elif usr_input2 == "4" :
            break
        else :
            print("Error! please 1 ,2 ,3 ,4")