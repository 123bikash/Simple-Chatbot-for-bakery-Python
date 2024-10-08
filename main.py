import re
import random

R_EATING = "I dont like eating anything anything because i am a bot obviously!"


def unknown():
    response = ['Could you please re-phrase that',
                "...",
                "Sounds about right",
                "what do you mean"][random.randrange(4)]
    return response


def message_probability(user_message, recognized_word, single_Response=False, required_words=[]):
    message_certainity= 0
    has_required_words= True
    
    
    # Counts how may wordes are present in each predefied message
    for word in user_message:
        if word in recognized_word:
            message_certainity +=1
    
    
    #calculates the percentage of recognized words in the user message
    percentage = float(message_certainity) / float(len(recognized_word))
    
    
    #checks that he required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break
    
    
    
    if has_required_words or single_Response:
        return int(percentage*100)
    else:
        return 0
    

def check_all_messages(message):
    highest_prob_list = {}
    
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Responses --------------------------------------------------------------->
    
    response('Hello!', ['hello', 'hi', 'sup', 'hey', 'heyo'], single_response=True)
    response('I want to order.', ['order', 'want to order', 'place an order', 'I would like to order', 'can I order'], required_words=['order'])
    response('We have different kinds of bread.', ['bread', 'what kind of bread', 'types of bread', 'do you have bread'], required_words=['bread'])
    response('We offer a variety of pastries.', ['pastries', 'what kind of pastries', 'types of pastries', 'do you have pastries'], required_words=['pastries'])
    response('What type of cake are you looking for?', ['cakes', 'birthday cake', 'wedding cake', 'custom cake', 'types of cakes'], required_words=['cakes'])
    response('Heres whats available today.', ['available', 'what\'s available', 'do you have', 'items in stock', 'what do you have today'], required_words=['available'])
    response('The price varies by item.', ['price', 'cost', 'how much', 'quote', 'what\'s the price', 'how much is'], required_words=['price'])
    response('Yes, we can deliver.', ['deliver', 'delivery', 'can you deliver', 'do you ship', 'shipping', 'delivery options'], required_words=['deliver'])
    response('You can pay by cash, credit, or debit.', ['payment', 'pay', 'bill', 'credit', 'debit', 'cash', 'how to pay'], required_words=['payment'])
    response('Our business hours are from 9 AM to 9 PM.', ['hours', 'open', 'opening times', 'closing time', 'when are you open', 'business hours'], required_words=['hours'])
    response('Our location is at 123 Baker Street.', ['location', 'address', 'where are you', 'how do I find you'], required_words=['location'])
    response('You can contact us at 555-1234.', ['contact', 'reach you', 'phone number', 'email'], required_words=['contact'])
    response('Heres whats on our menu.', ['menu', 'what\'s on your menu', 'items on the menu', 'what do you offer'], required_words=['menu'])
    response('Today\'s special is the chocolate cake.', ['specials', 'what\'s special today', 'today\'s special', 'any special offers'], required_words=['specials'])
    response('We have options for allergies.', ['allergies', 'allergy', 'do you have options for allergies'], required_words=['allergies'])
    response('Yes, we have gluten-free options.', ['gluten_free', 'gluten free', 'do you have gluten-free options'], required_words=['gluten_free'])
    response('Yes, we offer vegan options.', ['vegan', 'do you have vegan options'], required_words=['vegan'])
    response('Check out our current discounts.', ['discounts', 'discount', 'deal', 'promotion', 'any current deals'], required_words=['discounts'])
    response('You can subscribe to our newsletter.', ['subscribe', 'newsletter', 'how to subscribe'], required_words=['subscribe'])
    response('Yes, we do catering for events.', ['catering', 'events', 'do you cater', 'catering services'], required_words=['catering'])
    response('We can create a custom cake for you.', ['custom_cakes', 'custom cake', 'special cake', 'do you do custom cakes'], required_words=['custom_cakes'])
    response('You can check your order status here.', ['order_status', 'status', 'order status', 'check my order status'], required_words=['order_status'])
    response('For refunds, please refer to our return policy.', ['refund', 'return', 'how to get a refund', 'return policy'], required_words=['refund'])
    response('You can pick up your order here.', ['pickup', 'pick up', 'order for pickup'], required_words=['pickup'])
    response('Heres the list of ingredients.', ['ingredients', 'what\'s in', 'made of', 'ingredients list'], required_words=['ingredients'])
    response('We offer nut-free options.', ['nut_free', 'nut-free', 'nut free', 'do you have nut-free options'], required_words=['nut_free'])
    response('We have coffee, tea, and juice.', ['drinks', 'coffee', 'tea', 'juice', 'what drinks do you have'], required_words=['drinks'])
    response('We offer a variety of sandwiches.', ['sandwiches', 'sandwich', 'do you have sandwiches', 'types of sandwiches'], required_words=['sandwiches'])
    response('You can place a custom order with us.', ['custom_order', 'custom', 'special order', 'can I place a custom order'], required_words=['custom_order'])
    response('Happy birthday! We have special cakes.', ['birthday', 'birthday cake', 'birthday celebration'], required_words=['birthday'])
    response('We have beautiful wedding cakes.', ['wedding', 'wedding cake', 'for a wedding', 'wedding celebration'], required_words=['wedding'])
    response('We appreciate your feedback!', ['feedback', 'review', 'how was your service', 'what do you think'], required_words=['feedback'])


    response(R_EATING, ['what', 'you', 'eat'], required_words= ['you', 'eat'])
    best_match = max(highest_prob_list, key = highest_prob_list.get)
    # print(highest_prob_list)
    
    return unknown() if highest_prob_list[best_match] < 1 else best_match 
  

def get_response(user_input):
    split_message = re.split(r'\s+|[,;;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

#Testing the response system
while True:
    print('Bot: ' + get_response(input('You: ')))