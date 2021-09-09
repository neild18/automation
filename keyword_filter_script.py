import streamlit as st 
import pandas as pd
import re
import base64
import io
import time

def main():
	st.title("Gaming Keyword Filter Tool")
	st.text('Filter out all the irrelevant keywords from your downloads from your favourite keyword research tools!')
	st.subheader('What does this tool do?')
	st.text('1\. It will add new columns for \'Intent\', \'Games\',  and for gaming related \'Modifiers\'.')
	st.text('2\. It will create a column called \'Filter\' with Positive or Negative values. Positive being relevant keywords and Negative being irrelevant keywords.')
	st.warning('Make sure that the CSV contains a column titled \'Keyword\'. \'KEYWORD\' won\'t work. The keyword column is essential, otherwise the file won\'t work.')
	st.text('Once uploaded, go grab a brew (preferably something soft) while the file is being processed.')
	uploaded_file = st.file_uploader("Choose a file")
	if upload_file is not None:
		if upload_file.name[0][-4:] == 'xlsx':
			df = pd.read_excel(upload_file)
			st.dataframe(df)
		else:
			df = pd.read_csv(upload_file)
			st.dataframe(df)


		df.columns= df.columns.str.lower()
		df['keyword'] = df['keyword'].astype(str)
		def intent(keyword=""): 
		    learn = re.search(r'^(is |what |where |who |how |when|can)', keyword)
		    inform = re.search(r'(news|strategy|community| latest|forum(s)*|q(&| & | and )a| stor(y|ies)|interview|opinion|scoop|explaine(r|d)| post|digest|tutorial|course|guide|tips|review)', keyword)
		    compare = re.search(r'(best |top |compare|comparison|provider)', keyword)
		    play = re.search(r'(play|demo|free|game|online|mobile|download|bonus|code|live|money|payouts|pay outs)', keyword)
		    gamble = re.search(r'(deposit|pay[ ]*outs|real|bet|odds|betting)', keyword)
		    if learn:
		    	return 'learn'
		    elif inform:
		    	return 'Inform'
		    elif compare:
		    	return 'Compare'
		    elif play:
		    	return 'Play'
		    elif gamble:
		    	return 'Gamble'
		    else:
		    	return 'none'
		def modifier(keyword=""): 
		    free = re.search(r'free', keyword)
		    strategy = re.search(r'strategy', keyword)
		    calculator = re.search(r'calculator', keyword)
		    odds = re.search(r'odds', keyword)
		    tips = re.search(r'tips', keyword)
		    offers = re.search(r'offers', keyword)
		    deposit = re.search(r'deposit', keyword)
		    best = re.search(r'(top |best )', keyword)
		    live = re.search(r'live', keyword)
		    review = re.search(r'review', keyword)
		    download = re.search(r'download', keyword)
		    money = re.search(r'money', keyword)
		    mobile = re.search(r'(app |apps |android|iphone|mobile)', keyword)
		    online = re.search(r'online', keyword)
		    payout = re.search(r'(payout|pay out)', keyword)
		    highest = re.search(r'highest', keyword)
		    bonus = re.search(r'bonus', keyword)
		    codes = re.search(r'code', keyword)
		    wins = re.search(r'(win |wins )', keyword)
		    codes = re.search(r'code', keyword)
		    youtube = re.search(r'youtube', keyword)
		    video = re.search(r'video', keyword)
		    progressive = re.search(r'progressive', keyword)
		    year = re.search(r'201[0-9]{1}', keyword)
		    game = re.search(r'game', keyword)
		    bag = re.search(r'bag', keyword)
		    if free:
		    	return 'Free'
		    elif offers:
		    	return 'Offers'
		    elif strategy:
		    	return 'Strategy'
		    elif calculator:
		    	return 'Calculator'
		    elif odds:
		    	return 'Odds'
		    elif tips:
		    	return 'Tips'
		    elif deposit:
		    	return 'Deposit'
		    elif best:
		    	return 'Best'
		    elif live:
		    	return 'Live'
		    elif review:
		    	return 'Review'
		    elif download:
		    	return 'Downloads'
		    elif mobile:
		    	return 'mobile'
		    elif online:
		    	return 'Online'
		    elif payout:
		    	return 'Payout'
		    elif highest:
		    	return 'Highest'
		    elif wins:
		    	return 'Wins'
		    elif bonus:
		    	return 'Bonus'
		    elif bonus and codes:
		    	return 'Bonus_codes'
		    elif youtube:
		    	return 'Youtube'
		    elif video:
		    	return 'Video'
		    elif year:
		    	return 'Year'
		    elif bag:
		    	return 'Bag'
		    elif money:
		    	return 'Money'
		    else:
		    	return 'none'

		# Categorisation function which accepts x arguments
		def game(keyword=""): 
		    sport = re.search(r'(football|sport|cricket|nba|euros|nhl|baseball|basketball|nfl|soccer|ufc|boxing|euro 202(0|1|4|8)|world cup|tennis|hockey|esport|f1|olympics|superbowl|golf)', keyword)
		    poker = re.search(r'(poker|texas hold em|texas holdem|holdem)', keyword)
		    blackjack = re.search(r'blackjack', keyword)
		    roulette = re.search(r'roulette', keyword)
		    horse_racing = re.search(r'(horse racing|horse races)', keyword)
		    bingo = re.search(r'bingo', keyword)
		    slots = re.search(r'(slot|pokies|fruit machine)', keyword)
		    if sport:
		    	return 'sport'
		    elif poker:
		    	return 'poker'
		    elif blackjack:
		    	return 'blackjack'
		    elif roulette:
		    	return 'roulette'
		    elif horse_racing:
		    	return 'horse_racing'
		    elif bingo:
		    	return 'bingo'
		    elif slots:
		    	return 'slots'
		    else:
		    	return 'none'
		df['Intent'] = df.apply(lambda x: intent(x['keyword']), axis=1)
		df['Modifier'] = df.apply(lambda x: modifier(x['keyword']), axis=1)
		df['Game'] = df.apply(lambda x: game(x['keyword']), axis=1)

		certain_df = pd.read_csv('certain.csv')
		casinos_df = pd.read_csv('casinos.csv')
		deposits_df = pd.read_csv('deposit.csv')
		mobile_df = pd.read_csv('mobile.csv')
		slot_types_df = pd.read_csv('slot_types.csv')
		software_df = pd.read_csv('software.csv')
		games_df = pd.read_csv('games.csv')
		main_df = pd.read_csv('main.csv')
		location_df = pd.read_csv('location.csv')
		negative_df = pd.read_csv('negative.csv')

		certain = certain_df['Header'].values.tolist()
		negative = negative_df['Header'].values.tolist()
		casinos = casinos_df['Header'].values.tolist()
		deposit = deposits_df['Header'].values.tolist()
		mobile = mobile_df['Header'].values.tolist()
		games = games_df['Header'].values.tolist()
		slot_types = slot_types_df['Header'].values.tolist()
		software = software_df['Header'].values.tolist()
		main = main_df['Header'].values.tolist()
		location = location_df['Header'].values.tolist()

		keywords = casinos + deposit + mobile + software + games + slot_types + main
		words = [word for line in keywords for word in line.split()]
		certain_word = [word for line in certain for word in line.split()]
		casino_word = [word for line in casinos for word in line.split()]
		deposit_word = [word for line in deposit for word in line.split()]
		mobile_word = [word for line in mobile for word in line.split()]
		games_word = [word for line in games for word in line.split()]
		slot_types_word = [word for line in slot_types for word in line.split()]
		software_word = [word for line in software for word in line.split()]
		main_word = [word for line in main for word in line.split()]
		negative_word = [word for line in negative for word in line.split()]
		location_word = [word for line in location for word in line.split()]

		df['New'] = df['keyword'].str.split()
		#df['New'] = df['New'].astype(str).values.tolist()

		a_list = df['New']
		x = a_list[0]
		def cert(x): 
		    cw = any(item in certain_word for item in x)
		    if cw is True:
		    	return "True"
		    else:
		    	return "False"

		df['certain'] = df['New'].apply(lambda x: cert(x))

		a_list = df['New']
		x = a_list[0]
		def cw(x): 
		    cw = any(item in casino_word for item in x)
		    if cw is True:
		    	return "True"
		    else:
		    	return "False"

		df['casino'] = df['New'].apply(lambda x: cw(x))

		a_list = df['New']
		x = a_list[0]
		def dw(x):            
		    dw = any(item in deposit_word for item in x)
		    if dw is True:
		    	return "True"
		    else:
		    	return "False"

		df['deposits'] = df['New'].apply(lambda x: dw(x))

		a_list = df['New']
		x = a_list[0]
		def mw(x): 
		    mw = any(item in mobile_word for item in x)
		    if mw is True:
		    	return "True"
		    else:
		    	return "False"

		df['mobile'] = df['New'].apply(lambda x: mw(x))

		a_list = df['New']
		x = a_list[0]
		def gw(x): 
		    gw = any(item in games_word for item in x)
		    if gw is True:
		    	return "True"
		    else:
		    	return "False"

		df['games'] = df['New'].apply(lambda x: gw(x))

		a_list = df['New']
		x = a_list[0]
		def stw(x): 
		    stw = any(item in slot_types_word for item in x)
		    if stw is True:
		    	return "True"
		    else:
		    	return "False"

		df['slot_types'] = df['New'].apply(lambda x: stw(x))

		a_list = df['New']
		x = a_list[0]
		def sw(x): 
		    sw = any(item in software_word for item in x)
		    if sw is True:
		    	return "True"
		    else:
		    	return "False"

		df['software'] = df['New'].apply(lambda x: sw(x))

		a_list = df['New']
		x = a_list[0]
		def maw(x): 
		    maw = any(item in main_word for item in x)
		    if maw is True:
		    	return "True"
		    else:
			return "False"

		df['main'] = df['New'].apply(lambda x: maw(x))

		a_list = df['New']
		x = a_list[0]
		def loc(x): 
		    loc = any(item in location for item in x)
		    if loc is True:
			return "True"
		    else:
			return "False"

		df['location'] = df['New'].apply(lambda x: loc(x))

		a_list = df['New']
		x = a_list[0]
		def test(x="", y=""):
		    t = any(item in certain_word for item in x)
		    check =  all(item in words for item in x)
		    in_location = any(item in location for item in x)
		    negative_stopwords = any(item in negative_word for item in x)
		    if t is True:
			return "Positive"
		    elif negative_stopwords is True or in_location is True:
			return "Negative"
		    elif check is True:
			return "Positive"
		    else :
			return "Negative"

		#Lambda way of looping
		df['Filtered'] = df.apply(lambda x: test(x['New'], x['keyword']), axis=1)
		st.write(df) 

		timestr = time.strftime("%Y%m%d-%H%M%S")
		def csv_downloader(data):

			csvfile = data.to_csv()
			b64 = base64.b64encode(csvfile.encode()).decode()
			new_filename = "keyword_concat_output_{}_.csv".format(timestr)
			href = f'<a href="data:file/csv;base64,{b64}" download="{new_filename}">Download</a>'
			st.markdown(href,unsafe_allow_html=True)

		csv_downloader(df)



		

if __name__ == '__main__':
	main()
