from captcha.image import ImageCaptcha
from captcha.audio import AudioCaptcha
import string
import random
from PIL import Image
from playsound import playsound


def generate_image_captcha(word):
    """
    Function to generate the image captcha.
    :return:
    """
    image = ImageCaptcha(width=280, height=90)  # Store the captcha into a variable image and define its dimentions
    # data = image.generate(word)  # Will be the text on the captcha
    image.write(word, "demo.jpg")  # Generate the image and save it to the "demo.jpg" file


def text_generator(length):
    """
    Function to return a random word
    :param length: maximum length of the word, must be an integer
    :return:
    """
    letters = string.ascii_lowercase
    # numbers = string.digits  # TODO : Add numbers in the captcha
    arr = []
    for i in range(length):
        arr.append(random.choice(letters))
    return "".join(arr)


def random_number(length):
    """
    Generate random numbers
    :param length: number of random numbers generated
    :return:
    """
    arr = []
    numbers = string.digits
    for i in range(length):
        arr.append(random.choice(numbers))
    return "".join(arr)


def display_captcha(image):
    """
    Function called to display the captcha image
    :param image: name of the image TODO : Add a path to read the captcha
    :return:
    """
    photo = Image.open(image)
    photo.show()


def validate_captcha(word):
    """
    Function that requires the user input to check if the input is == to the captcha.
    :param word: word that has been generated for the captcha
    :return:
    """
    ans = input("please enter the CAPTCHA to continue : ")
    if ans == word:
        print("You're not a bot, have fun!")
    else:
        print("You're a robot scum, GETOUTAHERE.")


def generate_audio_captcha(numbers):
    """
    Function to generate the audio captcha.
    :param numbers: is what will be generated
    :return:
    """
    audio = AudioCaptcha()  # Store the captcha into a variable image
    audio.write(numbers, "demo.wav")


def play_audio_captcha(file):
    """
    Function used to play the audio captcha
    :param file: name of the file. TODO : Add the path of the captcha audio file
    :return:
    """
    playsound(file)


def validate_audio_captcha(numbers):
    """
    Function that requires the user input to check if the input is == to the captcha.
    :param numbers: number that has been generated for the audio captcha
    :return:
    """
    ans = input("please enter the CAPTCHA to continue : ")
    if ans == numbers:
        print("You're not a bot, have fun!")
    else:
        print("You're a robot scum, GETOUTAHERE.")


if __name__ == "__main__":
    word = text_generator(6)            #   Part used for
    generate_image_captcha(word)        #   generating and using
    display_captcha("demo.jpg")         #   a image captcha
    validate_captcha(word)              #   and verify it via user input()

    # numbers = random_number(4)            # Part used for
    # generate_audio_captcha(numbers)       # generating and using
    # play_audio_captcha("demo.wav")        # an audio captcha and
    # validate_audio_captcha(numbers)       # verify it via use input()
