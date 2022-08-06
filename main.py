import cv2
import pytesseract
from PIL import Image
from difflib import SequenceMatcher

def qualified_title(image):
    """This function will retreive the number of
    qualified people for the next round."""

    title_top = 40
    title_height = 180
    title_left = 550
    title_lenght = 1370

    cropped_title = image[title_top:title_height, title_left:title_lenght]
    gray_title = cv2.cvtColor(cropped_title, cv2.COLOR_BGR2GRAY)
    title = Image.fromarray(gray_title)

    text = pytesseract.image_to_string(title)

    return text

def players_boxes(image):
    """This function will retreive boxes of all
    qualified players"""

    player_top_top = 185
    player_top_bot = 290
    player_left_left = 410
    player_left_right = 500

    cropped_player = image[player_top_top:player_top_bot, player_left_left:player_left_right]
    gray_player = cv2.cvtColor(cropped_player, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Player', gray_player)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def players_names(image):
    """This function will retreive username of all
    qualified players"""

    usernames = []

    board_columns = 12
    board_rows = 5

    player_top_top = 185
    player_top_bot = 200
    player_left_left = 400
    player_left_right = 493
    
    for i in range(board_rows): 
        player_left_left = 400
        player_left_right = 493
        for y in range(board_columns):
            cropped_player = image[player_top_top:player_top_bot, player_left_left:player_left_right]
            gray_player = cv2.cvtColor(cropped_player, cv2.COLOR_BGR2GRAY)
            (thresh, black_and_white_player) = cv2.threshold(gray_player, 232, 200, cv2.THRESH_BINARY) # around 232, 233
            # cv2.imshow('Player', cropped_player)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()
            username_pic = Image.fromarray(black_and_white_player)
            username = pytesseract.image_to_string(username_pic)
            usernames.append(username.replace('\n',''))
            player_left_left += 93
            player_left_right += 93
        player_top_top += 104 # between 103 and 104
        player_top_bot += 104 # between 103 and 104
    
    return usernames

def compare_lists(list_a, list_b):
    """This method will compare two lists to get the percentage
    of success of the OCR"""

    if len(list_a) != len(list_b):
        print("Couldn't compare lists.")
    else:
        null_values=0
        ratios = 0
        for counter, value in enumerate(list_a):
            ratio = SequenceMatcher(None, value, list_b[counter]).ratio() * 100
            if value == '' and list_b[counter] == '':
                null_values+=1
            else:
                print(f'{value} => {list_b[counter]} : {ratio}%')
                ratios += ratio
       
        average_ratio = ratios/(len(list_a) - null_values)
        print(f'The average ratio is {average_ratio}.')


correct_usernames_fgafter = ['zvDaviid', 'Georgqw', 'pera-molte', '', '', '', 'justinchefwales', '', '', '', 'GoldenFreddy247', 'dark7700142',
                     'Raffipuffi', '', 'Nemanja255', 'polllito3', 'ilijalukin', 'ah4', '', 'le_playerpotter', '', '', 'einfachmalso_oko', 'BigturnSam'
                     '', 'BeauN1NJ4', 'LMAO-Sebo', 'DS_2_', 'lasheee14', 'GimmeYoFood2419', 'QuackTheDuck46', 'X-olaidana-X', '', 'Renzy_the_Psycho', '', 'Missydante',
                     'pavlelatin04', 'KhalVissi', '', 'Malek452', '', 'Nolansr02', 'piotrghost', 'FLASH Gordon070', 'Schnee_Krleger', 'Gnercad', 'SAMUNK', 'Black2_Car3',
                     'Firefist_AJ97', '', 'Senthu26', 'INQUIZIT', 'Roque-_-09', 'cours-rares', '', '', 'TSM_NAJJARF', 'M4jszakk_19', 'Ghosht_16', 'JackRapid5270']

original_image = cv2.imread('images/fgafter.png')
qualified = qualified_title(original_image)
print(qualified)
usernames = players_names(original_image)
compare_lists(correct_usernames_fgafter, usernames)
print(usernames)


