# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#import os
#import json
from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
app.config["DEBUG"]=True
api = Api(app)

novels = [
    {
         "id": "1",
        "name": "The Lost Symbol",
        "author": "Dan Brown",
        "blurb": "When Langdon’s beloved mentor, Peter Solomon–a prominent Mason and philanthropist–is brutally kidnapped, Langdon realizes his only hope of saving Peter is to accept this mystical invitation and follow wherever it leads him. Langdon is instantly plunged into a clandestine world of Masonic secrets, hidden history, and never-before-seen locations–all of which seem to be dragging him toward a single, inconceivable truth.",
        "genre": "Thriller"
    },
    {
         "id": "2",
        "name": "Da Vinci Code",
        "author": "Dan Brown",
        "blurb": "Langdon joins forces with a gifted French cryptologist, Sophie Neveu, and learns the late curator was involved in the Priory of Sion—an actual secret society whose members included Sir Isaac Newton, Botticelli, Victor Hugo, and da Vinci, among others. The Louvre curator has sacrificed his life to protect the Priory’s most sacred trust: the location of a vastly important religious relic, hidden for centuries."

                    + "In a breathless race through Paris, London, and beyond, Langdon and Neveu match wits with a faceless powerbroker who appears to work for Opus Dei—a clandestine, Vatican-sanctioned Catholic sect believed to have long plotted to seize the Priory’s secret. Unless Langdon and Neveu can decipher the labyrinthine puzzle in time, the Priory’s secret—and a stunning historical truth—will be lost forever.",
        "genre": "Historical fiction, Mystery"
    },
    {
         "id": "3",
        "name": "Inferno",
        "author": "Dan Brown",
        "blurb": "In the heart of Italy, Harvard professor of symbology Robert Langdon is drawn into a harrowing world centered on one of history’s most enduring and mysterious literary masterpieces . . . Dante’s Inferno."

+ "Against this backdrop, Langdon battles a chilling adversary and grapples with an ingenious riddle that pulls him into a landscape of classic art, secret passageways, and futuristic science. Drawing from Dante’s dark epic poem, Langdon races to find answers and decide whom to trust . . . before the world is irrevocably altered.",
        "genre": "Detective Fiction, Thriller"
    },
    {
         "id": "4",
        "name": "Origin",
        "author": "Dan Brown",
        "blurb": "Kirsch, who was one of Langdon’s first students at Harvard two decades earlier, is about to reveal an astonishing breakthrough . . . one that will answer two of the fundamental questions of human existence. As the event begins, Langdon and several hundred guests find themselves captivated by an utterly original presentation, which Langdon realizes will be far more controversial than he ever imagined. But the meticulously orchestrated evening suddenly erupts into chaos, and Kirsch’s precious discovery teeters on the brink of being lost forever. Reeling and facing an imminent threat, Langdon is forced into a desperate bid to escape Bilbao. With him is Ambra Vidal, the elegant museum director who worked with Kirsch to stage the provocative event. Together they flee to Barcelona on a perilous quest to locate a cryptic password that will unlock Kirsch’s secret. Navigating the dark corridors of hidden history and extreme religion, Langdon and Vidal must evade a tormented enemy whose all-knowing power seems to emanate from Spain’s Royal Palace itself . . . and who will stop at nothing to silence Edmond Kirsch. On a trail marked by modern art and enigmatic symbols, Langdon and Vidal uncover clues that ultimately bring them face-to-face with Kirsch’s shocking discovery . . . and the breathtaking truth that has long eluded us.",
        "genre": "Thriller"
    },
     {
          "id": "5",
        "name": "Angels & Demons",
        "author": "Dan Brown",
        "blurb": "Langdon’s worst fears are confirmed on the eve of the Vatican’s holy conclave, when a messenger of the Illuminati announces he has hidden an unstoppable time bomb at the very heart of Vatican City. With the countdown under way, Langdon jets to Rome to join forces with Vittoria Vetra, a beautiful and mysterious Italian scientist, to assist the Vatican in a desperate bid for survival."

                + "Embarking on a frantic hunt through sealed crypts, dangerous catacombs, deserted cathedrals, and even to the heart of the most secretive vault on earth, Langdon and Vetra follow a 400-year old trail of ancient symbols that snakes across Rome toward the long-forgotten Illuminati lair… a secret location that contains the only hope for Vatican salvation.",
        "genre": "Crime fiction, Mystery"
    },
    {
         "id": "6",
        "name": "Deception Point",
        "author": "Dan Brown",
        "blurb": "With the Oval Office in the balance, the President dispatches White House Intelligence analyst Rachel Sexton to the Milne Ice Shelf to verify the authenticity of the find. Accompanied by a team of experts, including the charismatic academic Michael Tolland, Rachel uncovers the unthinkable—evidence of scientific trickery—a bold deception that threatens to plunge the world into controversy."

+ "But before Rachel can contact the President, she and Michael are attacked by a deadly task force…a private team of assassins controlled by a mysterious powerbroker who will stop at nothing to hide the truth. Fleeing for their lives in an environment as desolate as it is lethal, they possess only one hope for survival: to find out who is behind this masterful ploy. The truth, they will learn, is the most shocking deception of all…",
        "genre": "Science fiction, Thriller"
    },
    {
         "id": "7",
        "name": "Eleven Minutes",
        "author": "Paulo Coelho",
        "blurb": "Eleven Minutes is the story of a young girl named Maria who leaves her Brazilian home to go to Geneva, Switzerland, in hopes of great adventure and great love. Her situation does not prove to be what she had hoped and she pursues a career in prostitution in order to make money quickly in order to return home.",
        "genre": "Fiction"
    },
    {
         "id": "8",
        "name": "The Alchemist",
        "author": "Paulo Coelho",
        "blurb": "The Alchemist tells the story of a young shepherd named Santiago who is able to find a treasure beyond his wildest dreams. Along the way, he learns to listen to his heart and, more importantly, realizes that his dreams, or his Personal Legend, are not just his but part of the Soul of the Universe.",
        "genre": "Fantasy Fiction, Drama"
    },
    {
         "id": "9",
        "name": "The Winner Stands Alone",
        "author": "Paulo Coelho",
        "blurb": " Igor, a psychopathic Russian mobile phone mogul; Ewa, formerly Igor's wife but now married to Hamid, a Middle Eastern fashion magnate; Jasmine, an African woman on the brink of a successful modeling career; American actress Gabriela, eager to land a leading film role; and an ambitious criminal detective, hoping to resolve the case of his life. The tale narrates the tension within and between the characters in a 24-hour period.",
        "genre": "Fiction"
    },
    {
         "id": "10",
        "name": "Turtles All the Way Down",
        "author": "John Green",
        "blurb": "It all begins with a fugitive billionaire and the promise of a cash reward. Turtles All the Way Down is about lifelong friendship, the intimacy of an unexpected reunion, Star Wars fan fiction, and tuatara. But at its heart is Aza Holmes, a young woman navigating daily existence within the ever-tightening spiral of her own thoughts."

+ "In his long-awaited return, John Green shares Aza's story with shattering, unflinching clarity.",
        "genre": "Young Adult Fiction"
    }
    
]

class Novel(Resource):
    def get(self, id):
        for novel in novels:
            if(id == novel["id"]):
                return novel, 200
        return "Novel not found", 404

    def post(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("name")
        parser.add_argument("author")
        parser.add_argument("blurb")
        parser.add_argument("genre")
        args = parser.parse_args()

        for novel in novels:
            if(id == novel["id"]):
                return "Novel with id {} already exists".format(id), 400

        novel = {
            "id": id,
            "name": args["name"],
            "author": args["author"],
            "blurb": args["blurb"],
            "genre": args["genre"]
        }
        novels.append(novel)
        return novel, 201

    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("name")
        parser.add_argument("author")
        parser.add_argument("blurb")
        parser.add_argument("genre")
        args = parser.parse_args()

        for novel in novels:
            if(id == novel["id"]):
                novel['name'] = args["name"]
                novel['author'] = args["author"]
                novel['blurb'] = args["blurb"]
                novel['genre'] = args["genre"]
                return novel, 200
        
        novel = {
            "id": id,
            "name": args["name"],
            "author": args["author"],
            "blurb": args["blurb"],
            "genre": args["genre"]
        }
        novels.append(novel)
        return novel, 201

    def delete(self, id):
        global novels
        novels = [novel for novel in novels if novel["id"] != id]
        return "{} is deleted.".format(id), 200
      
api.add_resource(Novel, "/novel/<string:id>")

app.run()
