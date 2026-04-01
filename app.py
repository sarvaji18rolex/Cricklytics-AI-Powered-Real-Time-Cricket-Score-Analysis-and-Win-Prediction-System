from flask import Flask, render_template, jsonify, request
import requests
import json
from datetime import datetime, timedelta
import random

app = Flask(__name__)

# CricAPI - Free tier available at cricapi.com
# Using cricbuzz-cricket rapidapi free tier as backup
API_KEY = "PUT_YOUR_OWN_API"

BASE_URL = "https://api.cricapi.com/v1"

def get_current_matches():
    try:
        url = f"{BASE_URL}/currentMatches?apikey={API_KEY}&offset=0"
        r = requests.get(url, timeout=10)
        data = r.json()
        if data.get("status") == "success":
            return data.get("data", [])
    except:
        pass
    return get_demo_matches()

def get_match_scorecard(match_id):
    try:
        url = f"{BASE_URL}/match_scorecard?apikey={API_KEY}&id={match_id}"
        r = requests.get(url, timeout=10)
        data = r.json()
        if data.get("status") == "success":
            return data.get("data", {})
    except:
        pass
    return get_demo_scorecard(match_id)

def get_series_list():
    try:
        url = f"{BASE_URL}/series?apikey={API_KEY}&offset=0"
        r = requests.get(url, timeout=10)
        data = r.json()
        if data.get("status") == "success":
            return data.get("data", [])
    except:
        pass
    return []

def get_demo_matches():
    return [
        {
            "id": "match_001",
            "name": "India vs Australia - 3rd ODI",
            "matchType": "odi",
            "status": "India won by 47 runs",
            "venue": "Wankhede Stadium, Mumbai",
            "date": "2026-04-01",
            "dateTimeGMT": "2026-04-01T09:00:00",
            "teams": ["India", "Australia"],
            "teamInfo": [
                {"name": "India", "shortname": "IND", "img": ""},
                {"name": "Australia", "shortname": "AUS", "img": ""}
            ],
            "score": [
                {"r": 287, "w": 6, "o": 50, "inning": "India Inning 1"},
                {"r": 240, "w": 10, "o": 47.3, "inning": "Australia Inning 1"}
            ],
            "tossWinner": "India",
            "tossChoice": "bat",
            "matchWinner": "India",
            "series_id": "icc_odi_series_2026"
        },
        {
            "id": "match_002",
            "name": "England vs South Africa - T20I",
            "matchType": "t20",
            "status": "South Africa won by 5 wickets",
            "venue": "The Oval, London",
            "date": "2026-04-01",
            "dateTimeGMT": "2026-04-01T14:00:00",
            "teams": ["England", "South Africa"],
            "teamInfo": [
                {"name": "England", "shortname": "ENG", "img": ""},
                {"name": "South Africa", "shortname": "SA", "img": ""}
            ],
            "score": [
                {"r": 168, "w": 8, "o": 20, "inning": "England Inning 1"},
                {"r": 172, "w": 5, "o": 19.2, "inning": "South Africa Inning 1"}
            ],
            "tossWinner": "South Africa",
            "tossChoice": "field",
            "matchWinner": "South Africa",
            "series_id": "t20i_series_2026"
        },
        {
            "id": "match_003",
            "name": "Pakistan vs New Zealand - 1st Test",
            "matchType": "test",
            "status": "Day 2 - Match in progress",
            "venue": "National Stadium, Karachi",
            "date": "2026-03-31",
            "dateTimeGMT": "2026-03-31T04:30:00",
            "teams": ["Pakistan", "New Zealand"],
            "teamInfo": [
                {"name": "Pakistan", "shortname": "PAK", "img": ""},
                {"name": "New Zealand", "shortname": "NZ", "img": ""}
            ],
            "score": [
                {"r": 342, "w": 10, "o": 95.4, "inning": "Pakistan Inning 1"},
                {"r": 156, "w": 4, "o": 52.0, "inning": "New Zealand Inning 1"}
            ],
            "tossWinner": "Pakistan",
            "tossChoice": "bat",
            "matchWinner": "",
            "series_id": "pak_nz_test_2026"
        },
        {
            "id": "match_004",
            "name": "West Indies vs Sri Lanka - 2nd ODI",
            "matchType": "odi",
            "status": "West Indies won by 23 runs",
            "venue": "Kensington Oval, Barbados",
            "date": "2026-03-30",
            "dateTimeGMT": "2026-03-30T18:00:00",
            "teams": ["West Indies", "Sri Lanka"],
            "teamInfo": [
                {"name": "West Indies", "shortname": "WI", "img": ""},
                {"name": "Sri Lanka", "shortname": "SL", "img": ""}
            ],
            "score": [
                {"r": 295, "w": 7, "o": 50, "inning": "West Indies Inning 1"},
                {"r": 272, "w": 10, "o": 49.1, "inning": "Sri Lanka Inning 1"}
            ],
            "tossWinner": "West Indies",
            "tossChoice": "bat",
            "matchWinner": "West Indies",
            "series_id": "wi_sl_odi_2026"
        }
    ]

def get_demo_scorecard(match_id):
    scorecards = {
        "match_001": {
            "id": "match_001",
            "name": "India vs Australia - 3rd ODI",
            "matchType": "odi",
            "status": "India won by 47 runs",
            "venue": "Wankhede Stadium, Mumbai",
            "date": "2026-04-01",
            "tossWinner": "India",
            "tossChoice": "bat",
            "matchWinner": "India",
            "teams": ["India", "Australia"],
            "score": [
                {"r": 287, "w": 6, "o": 50, "inning": "India Inning 1"},
                {"r": 240, "w": 10, "o": 47.3, "inning": "Australia Inning 1"}
            ],
            "scorecard": [
                {
                    "inning": "India Inning 1",
                    "batting": [
                        {"batsman": {"name": "Rohit Sharma"}, "r": 78, "b": 62, "4s": 9, "6s": 3, "sr": 125.8, "out-by": "c Smith b Hazlewood"},
                        {"batsman": {"name": "Shubman Gill"}, "r": 45, "b": 54, "4s": 5, "6s": 1, "sr": 83.3, "out-by": "b Starc"},
                        {"batsman": {"name": "Virat Kohli"}, "r": 92, "b": 88, "4s": 10, "6s": 2, "sr": 104.5, "out-by": "c Maxwell b Cummins"},
                        {"batsman": {"name": "Shreyas Iyer"}, "r": 34, "b": 29, "4s": 3, "6s": 2, "sr": 117.2, "out-by": "b Maxwell"},
                        {"batsman": {"name": "KL Rahul"}, "r": 28, "b": 22, "4s": 2, "6s": 1, "sr": 127.3, "out-by": "not out"},
                        {"batsman": {"name": "Hardik Pandya"}, "r": 10, "b": 8, "4s": 1, "6s": 0, "sr": 125.0, "out-by": "not out"},
                    ],
                    "bowling": [
                        {"bowler": {"name": "Mitchell Starc"}, "o": 10, "m": 0, "r": 52, "w": 2, "eco": 5.2},
                        {"bowler": {"name": "Josh Hazlewood"}, "o": 10, "m": 1, "r": 48, "w": 1, "eco": 4.8},
                        {"bowler": {"name": "Pat Cummins"}, "o": 10, "m": 0, "r": 60, "w": 1, "eco": 6.0},
                        {"bowler": {"name": "Glenn Maxwell"}, "o": 10, "m": 0, "r": 65, "w": 2, "eco": 6.5},
                        {"bowler": {"name": "Adam Zampa"}, "o": 10, "m": 1, "r": 62, "w": 0, "eco": 6.2},
                    ]
                },
                {
                    "inning": "Australia Inning 1",
                    "batting": [
                        {"batsman": {"name": "David Warner"}, "r": 42, "b": 38, "4s": 5, "6s": 2, "sr": 110.5, "out-by": "c Rohit b Bumrah"},
                        {"batsman": {"name": "Travis Head"}, "r": 67, "b": 58, "4s": 8, "6s": 2, "sr": 115.5, "out-by": "c Virat b Shami"},
                        {"batsman": {"name": "Steven Smith"}, "r": 55, "b": 72, "4s": 4, "6s": 1, "sr": 76.4, "out-by": "lbw b Jadeja"},
                        {"batsman": {"name": "Marnus Labuschagne"}, "r": 28, "b": 34, "4s": 2, "6s": 0, "sr": 82.4, "out-by": "c KL b Bumrah"},
                        {"batsman": {"name": "Glenn Maxwell"}, "r": 34, "b": 22, "4s": 3, "6s": 2, "sr": 154.5, "out-by": "b Hardik"},
                        {"batsman": {"name": "Alex Carey"}, "r": 14, "b": 18, "4s": 1, "6s": 0, "sr": 77.8, "out-by": "c Iyer b Shami"},
                    ],
                    "bowling": [
                        {"bowler": {"name": "Jasprit Bumrah"}, "o": 10, "m": 2, "r": 38, "w": 3, "eco": 3.8},
                        {"bowler": {"name": "Mohammed Shami"}, "o": 9.3, "m": 0, "r": 55, "w": 3, "eco": 5.8},
                        {"bowler": {"name": "Ravindra Jadeja"}, "o": 10, "m": 1, "r": 42, "w": 2, "eco": 4.2},
                        {"bowler": {"name": "Hardik Pandya"}, "o": 8, "m": 0, "r": 58, "w": 1, "eco": 7.3},
                        {"bowler": {"name": "Kuldeep Yadav"}, "o": 10, "m": 0, "r": 47, "w": 1, "eco": 4.7},
                    ]
                }
            ],
            "timeline": [
                {"over": 1, "team1_runs": 8, "team2_runs": 0, "wickets1": 0, "wickets2": 0},
                {"over": 5, "team1_runs": 42, "team2_runs": 0, "wickets1": 0, "wickets2": 0},
                {"over": 10, "team1_runs": 85, "team2_runs": 0, "wickets1": 1, "wickets2": 0},
                {"over": 15, "team1_runs": 125, "team2_runs": 0, "wickets1": 1, "wickets2": 0},
                {"over": 20, "team1_runs": 155, "team2_runs": 0, "wickets1": 2, "wickets2": 0},
                {"over": 25, "team1_runs": 185, "team2_runs": 0, "wickets1": 2, "wickets2": 0},
                {"over": 30, "team1_runs": 215, "team2_runs": 0, "wickets1": 3, "wickets2": 0},
                {"over": 35, "team1_runs": 238, "team2_runs": 0, "wickets1": 4, "wickets2": 0},
                {"over": 40, "team1_runs": 255, "team2_runs": 0, "wickets1": 4, "wickets2": 0},
                {"over": 45, "team1_runs": 272, "team2_runs": 0, "wickets1": 5, "wickets2": 0},
                {"over": 50, "team1_runs": 287, "team2_runs": 0, "wickets1": 6, "wickets2": 0},
                {"over": 5, "team1_runs": 287, "team2_runs": 38, "wickets1": 6, "wickets2": 0},
                {"over": 10, "team1_runs": 287, "team2_runs": 72, "wickets1": 6, "wickets2": 1},
                {"over": 15, "team1_runs": 287, "team2_runs": 108, "wickets1": 6, "wickets2": 2},
                {"over": 20, "team1_runs": 287, "team2_runs": 138, "wickets1": 6, "wickets2": 3},
                {"over": 25, "team1_runs": 287, "team2_runs": 165, "wickets1": 6, "wickets2": 4},
                {"over": 30, "team1_runs": 287, "team2_runs": 188, "wickets1": 6, "wickets2": 5},
                {"over": 35, "team1_runs": 287, "team2_runs": 205, "wickets1": 6, "wickets2": 6},
                {"over": 40, "team1_runs": 287, "team2_runs": 220, "wickets1": 6, "wickets2": 7},
                {"over": 45, "team1_runs": 287, "team2_runs": 232, "wickets1": 6, "wickets2": 8},
                {"over": "47.3", "team1_runs": 287, "team2_runs": 240, "wickets1": 6, "wickets2": 10},
            ]
        }
    }
    return scorecards.get(match_id, scorecards["match_001"])

def generate_win_probability(scorecard):
    """Generate win probability based on match data"""
    scores = scorecard.get("score", [])
    match_type = scorecard.get("matchType", "odi")
    teams = scorecard.get("teams", ["Team A", "Team B"])
    
    if len(scores) == 0:
        return {"team1": 50, "team2": 50, "team1_name": teams[0], "team2_name": teams[1] if len(teams) > 1 else "Team B"}
    
    if len(scores) >= 2:
        t1_runs = scores[0].get("r", 0)
        t2_runs = scores[1].get("r", 0)
        t2_wickets = scores[1].get("w", 0)
        t2_overs = scores[1].get("o", 0)
        
        target = t1_runs + 1
        runs_needed = target - t2_runs
        
        if match_type == "odi":
            total_overs = 50
        elif match_type == "t20":
            total_overs = 20
        else:
            total_overs = 90
            
        overs_left = total_overs - t2_overs
        wickets_left = 10 - t2_wickets
        
        if runs_needed <= 0:
            return {"team1": 5, "team2": 95, "team1_name": teams[0], "team2_name": teams[1]}
        
        required_rr = runs_needed / max(overs_left, 0.1)
        if overs_left > 0:
            current_rr = t2_runs / max(t2_overs, 0.1)
        else:
            current_rr = t2_runs
            
        advantage = (current_rr - required_rr) * 5 + (wickets_left / 10) * 30
        team2_prob = min(max(50 + advantage, 5), 95)
        
        return {
            "team1": round(100 - team2_prob, 1),
            "team2": round(team2_prob, 1),
            "team1_name": teams[0],
            "team2_name": teams[1] if len(teams) > 1 else "Team B",
            "required_rr": round(required_rr, 2),
            "current_rr": round(current_rr, 2),
            "runs_needed": runs_needed,
            "wickets_left": wickets_left,
            "overs_left": round(overs_left, 1)
        }
    
    return {"team1": 50, "team2": 50, "team1_name": teams[0], "team2_name": teams[1] if len(teams) > 1 else "Team B"}

def get_h2h_stats(team1, team2):
    """Generate head-to-head statistics"""
    h2h_data = {
        ("India", "Australia"): {
            "total": 148, "team1_wins": 73, "team2_wins": 68, "ties": 7,
            "last_5": ["IND", "AUS", "IND", "IND", "AUS"],
            "highest_score_t1": "418/5 (50 overs)",
            "highest_score_t2": "434/4 (50 overs)",
            "avg_score_t1": 267, "avg_score_t2": 249
        }
    }
    
    key = (team1, team2)
    reverse_key = (team2, team1)
    
    if key in h2h_data:
        return h2h_data[key]
    elif reverse_key in h2h_data:
        d = h2h_data[reverse_key].copy()
        d["team1_wins"], d["team2_wins"] = d["team2_wins"], d["team1_wins"]
        d["last_5"] = [team2[:3].upper() if x == team1[:3].upper() else team1[:3].upper() for x in d["last_5"]]
        return d
    
    total = random.randint(20, 120)
    t1_wins = random.randint(5, total - 5)
    t2_wins = random.randint(3, total - t1_wins - 2)
    ties = total - t1_wins - t2_wins
    
    teams_list = [team1[:3].upper(), team2[:3].upper()]
    last_5 = [random.choice(teams_list) for _ in range(5)]
    
    return {
        "total": total, "team1_wins": t1_wins, "team2_wins": t2_wins, "ties": ties,
        "last_5": last_5,
        "highest_score_t1": f"{random.randint(280, 420)}/{random.randint(4, 9)} (50 overs)",
        "highest_score_t2": f"{random.randint(260, 400)}/{random.randint(4, 9)} (50 overs)",
        "avg_score_t1": random.randint(220, 280),
        "avg_score_t2": random.randint(210, 270)
    }

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/matches")
def api_matches():
    matches = get_current_matches()
    return jsonify({"status": "success", "data": matches})

@app.route("/api/match/<match_id>")
def api_match(match_id):
    scorecard = get_match_scorecard(match_id)
    win_prob = generate_win_probability(scorecard)
    scorecard["win_probability"] = win_prob
    
    teams = scorecard.get("teams", ["Team A", "Team B"])
    if len(teams) >= 2:
        scorecard["h2h"] = get_h2h_stats(teams[0], teams[1])
    
    return jsonify({"status": "success", "data": scorecard})

@app.route("/api/live_commentary/<match_id>")
def live_commentary(match_id):
    events = [
        {"over": "47.2", "event": "FOUR!", "desc": "Brilliant cover drive by Warner, beats mid-off for a boundary!", "type": "boundary"},
        {"over": "47.1", "event": "OUT!", "desc": "Labuschagne caught at mid-wicket by Rohit off Bumrah's short ball!", "type": "wicket"},
        {"over": "46.6", "event": "DOT", "desc": "Shami fires in a yorker, Maxwell digs it out to point.", "type": "dot"},
        {"over": "46.5", "event": "SIX!", "desc": "Maxwell launches Shami over long-on! Massive hit!", "type": "six"},
        {"over": "46.4", "event": "2 RUNS", "desc": "Maxwell drives through covers for a comfortable two.", "type": "runs"},
        {"over": "46.3", "event": "DOT", "desc": "Shami beats Maxwell with a sharp inswinger!", "type": "dot"},
        {"over": "46.2", "event": "1 RUN", "desc": "Smith works it behind square leg for a single.", "type": "runs"},
        {"over": "46.1", "event": "FOUR!", "desc": "Smith pulls Shami over mid-wicket for a gorgeous boundary!", "type": "boundary"},
    ]
    return jsonify({"status": "success", "data": events})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
