__author__ = 'uchatterjee'
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time

ckey = 't98IOEYjRa96NNzfPavNyUBwK'
csecret = 's8rXfJPPET6Or3wmJfHMgSDovVeXj8zowH23G3cFgCqXYexQZh'
atoken = '1373683584-Hf2xfK4tExqbLbjCwxoX1To12RvMaAAPDuoZ7DM'
asecret = 'zEEIk4X3tfVua5I38qLk8LP5byMOGa7e7LsuZrZhqK9Sn'


class listener(StreamListener):
    def on_data(self, data):
        try:

            # print data

            tweet = data.split(',"text":"')[1].split('","source')[0]

            username = data.split(',"screen_name":"')[1].split('","location')[0]

##            location = data.split(',"location":"')[1].split('","url')[0]

            print username+'-->'+tweet

            saveThis = str(username+'-->'+tweet)
            saveFile = open('tweetOutput.csv', 'a')
            saveFile.write(saveThis)
            saveFile.write('\n')
            saveFile.close()
            return True
        except BaseException, e:
            print 'failed ondata,', str(e)
            time.sleep(5)

    def on_error(self, status):
        print status


auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=['ecig', 'ecigs', 'e-cig', 'ecigarette', 'e-cigarette', 'vaporfi', 'halocigs', 'halo cigs', 'migcigs', 'mig cigs', 'apolloecigs', 'apollo e cigs', 'v2cigs', 'southbeachsmoke', '777cigs', '777cig', 'vape', 'vapes','wick for electronic cigarette','electronic cigarette wholesale','electronic cigarette push button','electronic cigarette free sample free shipping','electronic cigarette chinese cigarettes for sale','electronic cigarette wholesale china','electronic cigarette manufacturer china',
'electronic hookah','e cigarette disposable','e cigarette new','electronic cigarette wholesale','electronic cigarette distributors','e-cigarette vending machine','e-cigarette battery',
'e-cigarette free sample','electronic cigarette saudi arabia','e cigarette manufacturers usa','electronic cigarette singapore','electronic cigarette in egypt',
'electronic cigarette germany','electronic cigarette display','electronic cigarette maker','e-cigarette battery','electronic cigarette dubai','e cigarette battery',
'e cigar','E-hookah','e-cigarette battery','electric cigarette machine','cigarette rolling machine','electronic cigarette battery','electronic cigarette case holder',
'e-cigarette wholesale distributor','e-cigarette mechanical mod','e cigarette starter kit','e-cigarette wholesale distributor','e cigarette wholesale','e-hookah herbal cigarette case'
,'electronic hookah wholesale','cigarette vending machines','cigarette rolling machine','cigarette case covers','cigarette pack cover','e cigarette disposable',
'disposable atomizer','disposable e-cigarette','disposable electronic cigarette','disposable ecigarette','Disposable e-cigarette','Disposable e cig',
'Disposable cigarette','Disposable electronic cigarette wholesale','buy electronic cigarette','vaporizer e cigarette','rainbow smoke cigarettes','colored smoke cigarette',
'china import electronic cigarettes','free sample cigarettes','new products for 2013','japan electronic cigarette','cheap e-cigarette','cheap electronic cigarette',
'health electronic cigarettes','name brand cigarettes','wholesale electronic cigaretes','wholesale e cigarette','wholesale e cig','electronic cigarette starter kit',
'electronic cigarette kit','e cigarette starter kit','e cigarette kit','electronic cigarette ego','ego e cigarettes','ego e cigarette wholesale','ego electronic cigarette battery',
'ego electroni cigarette charge','ego e cig battery','ego lcd battery','ego 650mah battery','ego variable battery','ego twist battery','variable voltage battery',
'ego variable voltage battery','e cig vaporizer','best vapor e cig','best e cigs','best e cigarette uk','electric cigrattes','best ecig','ecig batteries',
'electronic cigarettes manufacturers','e cigarette manufacturer','best quality e cig','new ego cigarette','ego-t uk','ego tank e cig','ego t cigarette',
'us e cig manufacturers','suppliers e-cigarette','us e cig suppliers','e cig suppliers','electronic cigarette suppliers','cheap e cigarette kits',
'cheap e cigarette','cheap e cig','usa e cigarette','e cigarete usa','health e cigarettes','health e cigarette uk','e health cigarette uk',
'e health cigarette suppliers','e health cigarettes','health ecig','ecig us','elektrisk cigaret','electronic cigaret','electric cigaret',
'ego e cigaret','free trial e cigarette','cartomizers 510','smoking e cigarette','smoking electronic cigarette','vapor e cig','cartomizer ecig','e cigs uk','uk e cigarette',
'uk e cig','uk e cigarette suppliers','wholesale e cigarette suppliers uk','disposable cartomizers','cheap electronic cigaretts','cheap e cigs','cheap e cigarettes',
'cheap e cig','cheap cartomizers uk','mini e cigarette','mini e cig','mini cigarette','mini electronic cigarettes','e cig vapor','ego clearomizer ce4','ego ce4 clearomizer',
'clearomizer ego ce4','clearomizers ce4','ego clearomizer ce5','ego ce5 clearomizer','clearomizer ce5','tank clearomizer','vivi nova tank clearomizer','vivi nova clearomizer',
'clearomizer vivi nova','ego transparent clearomizer','ego clearomizers','ego clearomiser','the best clearomizer','wholesale clearomizer','rebuildable clearomizer uk',
'ego rebuildable clearomizer','best rebuildable clearomizer','"long wick clearomizer"""','clearomizer mt3','ego clearomizer','ce4 clearomizer','ce5 clearomizer',
'ego-w clearomizer','vision clearomizer','ego-t clear atomizer','clear atomizer for ego','ce4 clear atomizer','ego-t atomizer','ego atomizer','ego-c atomizer',
'perfume atomizer','ultrasonic atomize','ego battery lcd','ego battery passthrough','ego battery charger','embossed ego battery','ego battery 650','ego battery twist',
'e cigarettes','e cigarette atomizer','e cigarette ego','e cigarette cartomizer','e cigarette refills','e cigarette battery','health e cigarette','electronic cigarette ego-t',
'electronic cigarettes','electronic cigarette ego','electronic cigarette case','electronic cigarette atomizer','electronic cigarette refills','e cigarette distributor china',
'e cigarette supplier','e cigs new technology','e cig wholesale supplier','e cigarette ego','e cigarette battery','e cigarette china','e cigarette 2013','e cigarette wholesale',
'ecigarette 2013','e cigarete','e cig mod','ecig','ecigarette','e cig','cigarette case','cigarette electronic','cigarette electronique','electroni cigarette manufacturer chin',
'pcc e cigarette','pcc electronic cigarette','pcc 510','pcc kit','cartomizer wholesale','cartomizer 510','caromizer kit','caromizer disposable','diposable e-cigarette',
'diposable ecig','diposable ecigarette','ego battery','ego clearomizer','ego electronic cigarette','ego-t','ego w','ego twist','ego ce4','e cigarette display stand',
'electronique cigarette','genesis atomizer','electronic cigarete','elektronic cigarette','electronic shisha','e shisha','electronic hookah','cigarette electronic',
'electronical cigarette','e-cig','cigarette electronique','electronic hookah pen wholesale','electronic manufacturer cigarette','ego-ce4','electronic cigarette china',
'vaporizer cigarette','electronic cigarettes accessory','electronic tobacco','sigaretta elettronica','e-cigarette battery wholesale china','rebuildable atomizer',
'cigarette tubes colored'])
