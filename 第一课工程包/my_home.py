'''我的主页'''
import streamlit as st
#from streamlit_drawable_canvas import st_canvas
from PIL import Image

#st(background_image = Image.open("宇宙.gif"))

page = st.sidebar.radio('Menu', ['My Hobbies And Friends', 'My Pictures Processing', 'My Magic Dictionary', 'Messages','Share My Life','All About Me','Others'])

def page_1():
    '''My Hobbies And Friends'''
    with open('Schnappi(Kairo Pop Mix).mp3','rb')as f:
        mymp3=f.read()
    st.audio(mymp3,format='audio/mp3',start_time=0)
    #st.image('Rainbow.png')
    st.write('My favorite books:')
    st.write('The Adventure Of the Wooden Doll')
    st.write('I like this book is because this book is about a wooden doll Hitty and her 100 years travel.Hitty‘s travel sometimes are happy,sometimes are pain,but she always smile and keep hapiness.After read this book,I often remember Hitty,look,she is smile,she is teaching us about happiness.')
    st.image('a.png')
    st.write('Mother Goose')
    st.write('This book have lot of simple and intersting English songs,it is a good choice for kids to learn English.I start to read this book in my childhood,until now,I still like this book.This book bring me happy and makes me love to learn English')
    st.image('MotherGoose.png')
    st.write('----------')
    st.write('My favorite games:')
    st.write('Can Your Pet')
    st.image('Can Your Pet.png')
    st.write('This game is a very cute game and it have a big surprise')
    st.write('http://canyour.pet')
    st.write('Algodoo')
    st.image('Algodoo.png')
    st.write('You may don’t know about this game,but it is the best game I ever seen.It mixed play,physics and programming.You can make anything in this game with your imagination and creatively.')
    st.write('www.algodoo.com')
    
    st.write('-----------')
    st.write('My favorite TV show:')
    st.write('Dora The Explore')
    st.image('Dora.png')
    st.write('In this TV show,Dora is a 7 years old girl.It‘s about Dora and her monkey friend Boots and their explorer.Dora is a friendly girl,she helped lots of little animals or people that in trouble.')
    st.write('My Little Pony')
    st.image('b.png')
    st.write('This TV show tell us,friendly really have magic.These little pony is very good friends,and they will teach us how to be friendly')
    st.write('Hello Teddy')
    st.image('Teddy.png')
    st.write('In this TV show,I learn a lot of English,it is a really good choice foe young children.')
    st.write('----------')
    st.write('My friends')
    st.write('Semiya')
    st.image('Semiya.jpg')
    st.write('In July 2024,I had a travel to America.I make some friends like Semiya.Semiya is a 11 years old girl.I like to play toys with Semiya')
    st.write('True')
    st.image('True.jpg')
    st.write('Same as Semiya,I met True in July too.True is a 4 years old boy,he is very cute,I still remember he’s playing with me.True is an angel,thanks for give me those happy times. ')
    st.write('Tyce')
    st.image('Tyce.jpg')
    st.write('Same,I met Tyce in July.She is a 2 years old girl.She is very cute.')
def img_change(img,rc,gc,bc):
    width,height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x,y][rc]
            g = img_array[x,y][gc]
            b = img_array[x,y][bc]
            img_array[x,y] = (r,g,b)
    return img
def page_2():
    '''My Pictures Processing'''
    st.write('Amazing Sunglasses')
    uploaded_file = st.file_uploader("pictures",type=['jpg','jpeg','png'])
    if uploaded_file:
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        st.image(img)
        st.image(img_change(img,1,2,0))

def page_3():
    '''My Magic Dictionary'''
    st.write('My Magic Dictionary')
    with open('words_space.txt','r',encoding='utf-8') as f:
        words_list = f.read().split('\n')
        print(words_list)
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]),i[2]]
    with open('check_out_times.txt','r',encoding='utf-8') as f:
        times_list = f.read().split('\n')
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split('#')
    times_dict = {}
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])
    word = st.text_input('write words here')
    if word in words_dict:
        st.write(words_dict[word][1])
        n = words_dict[word][0]
        if n in times_dict:
            times_dict[n] += 1
        else:
            times_dict[n] = 1
        with open('check_out_times.txt','w',encoding='utf-8') as f:
            message = ''
            for k,v in times_dict.items():
                message += str(k) + '#' + str(v) +'\n'
            message = message[:-1]
            f.write(message)
        st.write('You translate this word',times_dict[n],'times')
        if word == 'snow':
            st.snow()
        if word == 'balloon':
            st.balloons()

def page_4():
    '''Messages'''
    st.write('messages')
    with open('leave_messages.txt','r',encoding='utf-8') as f:
        messages_list = f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split('#')
    for i in messages_list:
        if i[1] == 'Allen':
            with st.chat_message('💬'):
                st.write(i[1],':',i[2])
        elif i[1] == 'Semiya':
            with st.chat_message('💬'):
                st.write(i[1],':',i[2])
        elif i[1] == 'True':
            with st.chat_message('💬'):
                st.write(i[1],':',i[2])
        elif i[1] == 'Tyce':
            with st.chat_message('💬'):
                st.write(i[1],':',i[2])
    name = st.selectbox('I am...',['Allen','Semiya','True','Tyce','Other person'])
    new_message = st.text_input('I want to say...')
    if st.button('message'):
        messages_list.append([str(int(messages_list[-1][0])+1),name,new_message])
        with open('leave_messages.txt','w',encoding='utf-8') as f:
            message = ''
            for i in messages_list:
                message += i[0] + '#' + i[1] + '#' + i[2] + '\n'
            message = message[:-1]
            f.write(message)

def page_5():
    '''Share My Life'''
    st.write('July 14 2024,I had a travel to America.That‘s my first time to America,everything looks amazing.')

def page_6():
    '''All About Me'''
    st.write('Name：Allen')
    st.write('Age：13')
    st.write('Grade：7')
    st.write('Birthday：April-15-2011')
    st.write('Favorite Animals：Rabbits')
    st.write('My Favorite Color：Pink')
    st.write('My YouTube and Gmail')
    go = st.selectbox('Thank you', ['My YouTube', 'My Gmail'])
    if go == 'My YouTube':
        st.link_button('Subscribe me!', 'www.youtube.com/@LittleRabbitAllen')
    elif go == 'My Gmail':
        st.link_button('You can send emails to me', 'schweigartfusca@gmail.com')

def page_7():
    '''Others'''
    msg_lst1 = ['message1', 'message2', 'message3', 'message4', 'message5', 'message6', 'message7', 'message8']
    begin, end = st.slider('Choose：', 1, len(msg_lst1), (1, len(msg_lst1)))
    for i in range(begin-1, end):
        st.write(msg_lst1[i])
    st.write('----')
    number1 = st.slider('Number1：', 1, 100, 50)
    number2, number3 = st.slider('Number2 and 3：', 1, 10, (4, 6))
    st.write('Number1：', number1)
    st.write('Number2 and 3：', number2, '-', number3)    
    st.write('----')
    msg_lst = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Purple']
    begin, end = st.slider('Choose the rainbow you want：', 1, len(msg_lst), (1, len(msg_lst)))
    message = ''
    for i in range(begin-1,end):
        message += msg_lst[i]
        message += " "
    st.write(message)
    st.write('----')
    color = st.radio(
        'Which Color Is My Favorite?',
        ['I don’t know', 'Purple', 'Pink','Orange'],
        captions=['A', 'B', 'C','D']
    )
    message = ''
    if color =='Orange':
        message = 'Wrong!'
    elif color == 'Purple':
        message = 'Wrong!'
    elif color == 'Pink':
        message = 'Yes!'
    elif color == 'I don‘t know':
        message = 'Choose other!'
    st.write(message)

    
    
if page == 'My Hobbies And Friends':
    page_1()
elif page == 'My Pictures Processing':
    page_2()
elif page == 'My Magic Dictionary':
    page_3()
elif page == 'Messages':
    page_4()
elif page == 'Share My Life':
    page_5()
elif page == 'All About Me':
    page_6()
elif page == 'Others':
    page_7()

#python -m streamlit run my_home.py