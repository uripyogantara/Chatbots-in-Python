import re
pattern="mai kampus (.*)"
#
message="wee kajfls mai kampus cuk, ade bigmom dini"
#
match=re.match(pattern,message)
#
if match:
    print(match.group(0))
#
# pattern="if (.*)"
#
# message="what would happer if bots took over the world"
#
# match=re.search(pattern,message)
#
# # print(type(match.group(0)))
# print(match.group(0))
# print(match.group(1))
# TEMPLATE="How could I forget {}"
bot_template = "BOT : {0}"
response_template="How could I forget {0}"
user_template = "USER : {0}"
def swap_pronouns(phrase):
    if 'I' in phrase:
        phrase=re.sub("I","You",phrase)

    if 'me' in phrase:
        phrase=re.sub("me","you",phrase)

    if("my") in phrase:
        return re.sub("my","your",phrase)
    else:
        return phrase

def respond(message):
    # Concatenate the user's message to the end of a standard bot respone
    pattern="do you remember (.*)"
    match = re.search(pattern,message)
    print(match)
    if match:
        phrase=re.search(pattern,message).group(1).replace("?","")
        return response_template.format(swap_pronouns(phrase))
    else:
        return "i dont know  about that"
    # print(bot_message)
    # Return the result

# Define a function that sends a message to the bot: send_message
def send_message(message):
    # Print user_template including the user_message
    print(user_template.format(message))
    # Get the bot's response to the message
    response = respond(message)
    # print(response)
    # Print the bot template including the bot's response.
    print(bot_template.format(response))

send_message("do you remember me?")
# print(swap_pronouns("I walk with my Dog"))