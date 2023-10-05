import requests
import time
import json

import valclient.exceptions
from valclient.client import Client

running = True
stats = True
client = Client(region="na")
client.activate()

seenPregame = []
seenMatches = []

agentMap = {
    "add6443a-41bd-e414-f6ad-e58d267f4e95": "Jett",
    "a3bfb853-43b2-7238-a4f1-ad90e9e46bcc": "Reyna",
    "f94c3b30-42be-e959-889c-5aa313dba261": "Raze",
    "7f94d92c-4234-0a36-9646-3a87eb8b5c89": "Yoru",
    "eb93336a-449b-9c1b-0a54-a891f7921d69": "Phoenix",
    "bb2a4828-46eb-8cd1-e765-15848195d751": "Neon",
    "5f8d3a7f-467b-97f3-062c-13acf203c006": "Breach",
    "6f2a04ca-43e0-be17-7f36-b3908627744d": "Skye",
    "320b2a48-4d9b-a075-30f1-1f93a9b638fa": "Sova",
    "601dbbe7-43ce-be57-2a40-4abd24953621": "Kayo",
    "1e58de9c-4950-5125-93e9-a0aee9f98746": "Killjoy",
    "117ed9e3-49f3-6512-3ccf-0cada7e3823b": "Cypher",
    "569fdd95-4d10-43ab-ca70-79becc718b46": "Sage",
    "22697a3d-45bf-8dd7-4fec-84a9e28c69d7": "Chamber",
    "8e253930-4c05-31dd-1b6c-968525494517": "Omen",
    "9f0d8ba9-4140-b941-57d3-a7ad57c6b417": "Brimstone",
    "41fb69c1-4189-7b37-f117-bcaf1e96f1bf": "Astra",
    "707eab51-4836-f488-046a-cda6bf494859": "Viper",
    "dade69b4-4f5a-8528-247b-219e5a1facd6": "Fade",
    "95b78ed7-4637-86d9-7e41-71ba8c293152": "Harbor",
    "e370fa57-4757-3604-3648-499e1f642d3f": "Gekko"
}
teamMap = {
    "Blue": "DEFENDING",
    "Red": "ATTACKING"
}
streamer_dict = {
    "pandejalea": "pandejalea1",
    "riku": "rikugoat",
    "100tcryo": "cryocells",
    "100tbang": "bangzerra",
    "100tderrek": "derrekow",
    "100tasuna": "asunaweeb",
    "100tstellar": "stellar",
    "brax": "brax",
    "johnqt": "johnqtcs",
    "brawk": "brawk",
    "n4rrate": "n4rrate",
    "sillysalamander7": "acez2k",
    "srtdawgg": "tdawggwow",
    "lumizzy": "lumao",
    "t1ban": "ban_val",
    "eshotz": "eshotz",
    "moonblue": "moonbluetv",
    "jimmyjam": "jimmyjam_",
    "ange": "angee",
    "v1sarah": "sarahcantaim",
    "bucky": "buckyyfps",
    "bearkun": "bearkun",
    "gabesu": "gabesu",
    "snirott": "snirott",
    "lunafox": "the_lunafox",
    "g2dapr": "dapr",
    "ofda40": "dog_val",
    "40adr": "40adr",
    "nurfed": "nurfed25",
    "fpsdeny": "deny",
    "racoone": "theracoone",
    "addison": "addison",
    "shiro": "shirorz",
    "oradio": "oradio",
    "khoi": "khoima",
    "mrcipe": "mrcipe",
    "shamson": "shamson",
    "senshahzam": "shahzam",
    "eggster": "eggsterr_",
    "add3r": "add3rtv",
    "toeknee": "toeknee",
    "wardell": "wardell",
    "jollztv": "jollztv",
    "soop": "sooptv",
    "gilee": "gilee",
    "branted": "branted",
    "nolan1z": "nolan1z",
    "purevns": "purevns",
    "alkhovik": "alkhovik",
    "primemcd": "primemcd",
    "jakobeval": "jakobeval",
    "jawgemo": "jawgemo",
    "sinatraa": "sinatraa",
    "kade44": "kadeval44",
    "andrewonyx": "andrewonyx",
    "jerrwin": "jerrwin",
    "swagcon": "swagcon",
    "guacs": "guacs",
    "fazeshanks": "shanks_ttv",
    "c9zellsis": "zellsis",
    "iitztimmy": "iitztimmy",
    "a2guapo": "a2guapo",
    "keeoh": "keeoh",
    "huynh": "huynh",
    "bong bong": "bongbongna",
    "governor": "governor",
    "c4lpyso": "c4lypso_",
    "egbcj": "thebcj",
    "allusionstv": "allusionsttv",
    "zead": "zeadfps",
    "grim": "grimm",
    "ion2x": "ion2x",
    "fsvirtyy": "virtyy",
    "zombs": "zombs",
    "screwface": "screwfaceval",
    "yay": "yayster",
    "kanpeki": "kanpeki",
    "srbenita": "benita",
    "babyj": "babyj",
    "lukie": "lukie",
    "shawnbm": "shawnbm",
    "decay": "decayval",
    "blank": "blankaims",
    "1frog1": "1frog1",
    "f1ukie": "f1ukie",
    "amc": "a_m_c",
    "orisatty": "sattyfps",
    "sadriigz": "riigz_",
    "3dwn": "3dwn",
    "murked": "murkedval",
    "cookie": "cooki1e",
    "dartshooter77386": "dartshooter77386",
    "kmlord": "kmlord",
    "rythm": "rythmval",
    "welyy4": "welyy",
    "colt": "coltgg",
    "tnxdrago": "drago747",
    "mello": "mello_diy",
    "enza": "enzafps",
    "ether": "etherval",
    "shiphtur": "shiphtur",
    "symetrical": "symetrical",
    "xsetashley": "ashleybtw",
    "outlier": "ouutlier",
    "root": "root",
    "krakenniv": "krakenniv",
    "fairy": "fairyvalorant",
    "Jjfkslowpeekedop": "pr0phie",
    "dcplpyth0n": "pyth0n_val",
    "kazzan": "kazzanfps",
    "skully": "skullyjai",
    "bawnix": "bawnix",
    "barrytine": "barrytine",
    "chubsta": "thechubsta7",
    "lbsukimchi": "spicymangopie",
    "oxidizedf": "oxidizedf",
    "celocity": "velocityval",
    "tpgtyphon": "typhon_sin",
    "ccgunslinger": "ccgunslinger",
    "zerona": "zeronaaa",
    "sh4rp": "sh4rpshoo7er",
    "balooz": "balooz_",
    "t1munchkin": "munchking",
    "wedid": "wedidvalorant",
    "watson": "rsolos",
    "cryptx": "cryptx",
    "kiara": "415kiara",
    "darrin": "darrinval",
    "aztkk": "aztkk",
    "jerk": "jerktbe",
    "riceballinnn": "riceballinnn",
    "aniemal": "aniemal",
    "opted": "optedval",
    "sempiestar": "anylove_",
    "flexinnty": "flexinnty",
    "jay park": "traeyong",
    "okeanos": "okeanosqt",
    "jwordn": "jwordn",
    "jaomock": "jaomock",
    "ruckyducky": "ruckuh",
    "ghostcece": "cecee",
    "stronglegs": "stronglegs",
    "lrrykinn": "rykinn",
    "elijah": "elijah_val",
    "script": "fpsscript",
    "103saac": "103isaac",
    "RF jayymilz": "jayymilz",
    "løgan": "loganfake",
    "5ksleepy": "sleepycribb",
    "azgue": "azgue",
    "beansip": "beansip1",
    "7urg": "zurg",
    "jowzerra": "jowzerra",
    "xnb": "xnbfn",
    "rukitter": "rukitter",
    "thund3r": "thund3rval_",
    "br9dy": "br9dyval",
    "notexxd": "notexxdval",
    "psalm": "psalm",
    "firefps": "firefps_",
    "anniversary": "anniversary",
    "gordon405": "gordon405",
    "sukhdeep": "deepfps",
    "gamer": "gamer",
    "curry": "curry",
    "career": "career",
    "predsu": "predsu",
    "dasnerth": "dasnerth",
    "stohla": "stohla",
    "exalt": "exalt",
    "bobovo": "bobovo",
    "haanzer": "haanzer",
    "bobbert": "bobbert_val",
    "joe": "joedabozo",
    "cheri": "cheri",
    "wackypenguin22": "slushyval",
    "vajudgevynawp": "vyngg",
    "dsgsteel": "steel_tv",
    "rampage": "rampage",
    "maple": "mapletrhe",
    "rabaa": "raabaval",
    "igmtranspare": "transpare",
    "temet": "temet",
    "jayyron": "jayyrons",
    "tofu": "rltofu",
    "itscyndaquil": "itscyndaquil",
    "mistuhe": "mistuhe",
    "banhbao": "banhbaoval",
    "dittoblob13": "dittoblob13"
}
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
}

banner = '''

  ██████ ▄▄▄█████▓ ██▀███  ▓█████ ▄▄▄       ███▄ ▄███▓        ██████  ██▓███ ▓██   ██▓   
▒██    ▒ ▓  ██▒ ▓▒▓██ ▒ ██▒▓█   ▀▒████▄    ▓██▒▀█▀ ██▒      ▒██    ▒ ▓██░  ██▒▒██  ██▒   
░ ▓██▄   ▒ ▓██░ ▒░▓██ ░▄█ ▒▒███  ▒██  ▀█▄  ▓██    ▓██░      ░ ▓██▄   ▓██░ ██▓▒ ▒██ ██░   
  ▒   ██▒░ ▓██▓ ░ ▒██▀▀█▄  ▒▓█  ▄░██▄▄▄▄██ ▒██    ▒██         ▒   ██▒▒██▄█▓▒ ▒ ░ ▐██▓░   
▒██████▒▒  ▒██▒ ░ ░██▓ ▒██▒░▒████▒▓█   ▓██▒▒██▒   ░██▒      ▒██████▒▒▒██▒ ░  ░ ░ ██▒▓░   
▒ ▒▓▒ ▒ ░  ▒ ░░   ░ ▒▓ ░▒▓░░░ ▒░ ░▒▒   ▓▒█░░ ▒░   ░  ░      ▒ ▒▓▒ ▒ ░▒▓▒░ ░  ░  ██▒▒▒    
░ ░▒  ░ ░    ░      ░▒ ░ ▒░ ░ ░  ░ ▒   ▒▒ ░░  ░      ░      ░ ░▒  ░ ░░▒ ░     ▓██ ░▒░    
░  ░  ░    ░        ░░   ░    ░    ░   ▒   ░      ░         ░  ░  ░  ░░       ▒ ▒ ░░     
      ░              ░        ░  ░     ░  ░       ░               ░           ░ ░        
                                                                              ░ ░      
'''
print(banner)


def get_stats(url, check=stats):
    """ Gets player stats from dak.gg (tracker.gg uses web scraping protection). """

    r_ini = requests.get(url, headers=HEADERS)
    if check:
        try:
            dak_puuid = json.loads(r_ini.text)["account"]["puuid"]
            seasons_url = f"https://val.dakgg.io/api/v1/accounts/{dak_puuid}/seasons"
            r_seasons = requests.get(seasons_url, headers=HEADERS)
            current_season = json.loads(r_seasons.text)["seasons"][0]["season"]
            full_url = f"https://val.dakgg.io/api/v1/accounts/{dak_puuid}/seasons/{current_season}"
            r_stats = requests.get(full_url, headers=HEADERS)
            player_info = json.loads(r_stats.text)
            adr = round(
                player_info["stats"]["competitive"]["damage"] / player_info["stats"]["competitive"]["roundsPlayed"])
            rr = player_info["stats"]["competitive"]["rankedRating"]
            wins = player_info["stats"]["competitive"]["wins"]
            wr = round(
                (wins / (wins + player_info["stats"]["competitive"]["losses"] + player_info["stats"]["competitive"][
                    "draws"]) * 100), 1)
        except KeyError:
            return "Could not retrieve competitive stats for this player."
        return f"{adr} ADR | {wr}% Win Rate | {wins} Wins | {rr} RR"
    else:
        return "Stats disabled."


def reveal_names(puuid, agentID):
    """ Lists player names in agent select and live game, as well as their stats (if enabled) and tracker link. """

    playerData = client.put(
        endpoint="/name-service/v2/players",
        endpoint_type="pd",
        json_data=[puuid]
    )[0]
    ini_url = f"https://val.dakgg.io/api/v1/accounts/{playerData['GameName'].replace(' ', '')}-{playerData['TagLine']}"
    player_stats = get_stats(ini_url)
    name = playerData['GameName'].replace(' ', '%20')
    tracker_url = f"https://tracker.gg/valorant/profile/riot/{name}%23{playerData['TagLine']}/overview"
    if agentID == '':
        print(f"{playerData['GameName']}#{playerData['TagLine']} | STATS | {player_stats} | {tracker_url}")
    else:
        agent = agentMap[agentID]
        print(f"{playerData['GameName']}#{playerData['TagLine']} ({agent}) | STATS | {player_stats} | {tracker_url}")
        return playerData['GameName']


def find_streams(name):
    """ Searches for twitch streams, works best in high elo. """

    name = name.lower().strip()
    name = name.replace('twitch', '')
    name = name.replace('ttv', '')
    name_u = name.replace(' ', '_')
    name = name.replace(' ', '')
    if name in streamer_dict:
        twitch_name = streamer_dict[name]
        state = requests.get(f'https://twitch.tv/{twitch_name}').content.decode('utf-8')
        if 'isLiveBroadcast' in state:
            print(f'https://twitch.tv/{twitch_name}')

    potential_names = [f"{name}", f"{name_u}", f"{name}fps", f"{name}_val",
                       f"{name}val", f"{name}tv", f"{name_u}fps", f"{name_u}_val",
                       f"{name_u}val"]
    for streamers in potential_names:
        state = requests.get(f'https://twitch.tv/{streamers}').content.decode('utf-8')
        if 'isLiveBroadcast' in state:
            print(f'https://twitch.tv/{streamers}')


print("Waiting to find game.")
while running:
    time.sleep(10)
    sessionState = client.fetch_presence(client.puuid)['sessionLoopState']

    if sessionState == "PREGAME":
        try:
            matchID = client.pregame_fetch_player()['MatchID']
            if matchID not in seenPregame:
                seenPregame.append(matchID)
                matchInfo = client.pregame_fetch_match(matchID)
                # os.system('cls' if os.name == 'nt' else 'clear') #import os first
                print("\n" + "-" * 40 + " AGENT SELECT " + "-" * 40)
                print(f"Starting Side: {teamMap[matchInfo['Teams'][0]['TeamID']]}")
                for player in matchInfo['AllyTeam']['Players']:
                    puuid = player['Subject'].lower()
                    agentID = player['CharacterID'].lower()
                    reveal_names(puuid, agentID)
        except valclient.exceptions.PhaseError:
            pass

    elif sessionState == "INGAME":
        try:
            matchID = client.coregame_fetch_player()['MatchID']
            players = []
            if matchID not in seenMatches:
                seenMatches.append(matchID)
                matchInfo = client.coregame_fetch_match(matchID)
                # os.system('cls' if os.name == 'nt' else 'clear')
                print("\n" + "-" * 40 + " LIVE GAME " + "-" * 40)
                teamCounter = None
                for player in matchInfo['Players']:
                    team = player['TeamID']
                    if team != teamCounter:
                        print(f"\n{teamMap[team]}")
                    puuid = player['Subject'].lower()
                    agentID = player['CharacterID'].lower()
                    teamCounter = team
                    player = reveal_names(puuid, agentID)
                    players.append(player)

                print("\nFinding Streamers...")
                for names in players:
                    find_streams(names)
                print("Done.")
        except valclient.exceptions.PhaseError:
            pass