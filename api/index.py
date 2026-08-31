from fastapi import FastAPI, HTTPException, Header, Query
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Simple Book API",
    description="A beginner-friendly REST API containing information about books.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# BOOK DATA
books = [

    {
        "id": 1,
        "title": "The Count of Monte Cristo",
        "author": "Alexandre Dumas",
        "year": "1846",
        "genre": "Adventure",
        "rating": 4.34,
        "logline": "Edmund Dantes seeks to dismantle the lives of the ones who wrongfully imprisoned him for their gain.",
        "publisher": "Pétion",
        "maincharacters": "Edmond Dantès, Fernand Mondego, Danglars, Gérard de Villefort",
        "audiobook-duration": "52 Hours and 41 Minutes",
        "page-number": "1,276",
        "wordcount": "468,023",
        "language": "French",
        "synopsis": "Thrown in prison for a crime he has not committed, Edmond Dantes is confined to the grim fortress of If. There he learns of a great hoard of treasure hidden on the Isle of Monte Cristo and becomes determined not only to escape but to unearth the treasure and use it to plot the destruction of the three men responsible for his incarceration.",
        "publication-place": "France",
        "img-link": "https://m.media-amazon.com/images/S/compressed.photo.goodreads.com/books/1724863997i/7126.jpg"
    },

    {
        "id": 2,
        "title": "The Three Musketeers",
        "author": "Alexandre Dumas",
        "year": "1844",
        "genre": "Adventure",
        "rating": 4.1,
        "logline": "The story recounts the adventures of a young man named d'Artagnan after he leaves home to travel to Paris, hoping to join the Musketeers of the Guard.",
        "publisher": "Modern Library",
        "maincharacters": "d'Artagnan, Athos, Porthos, and Aramis",
        "audiobook-duration": "19 Hours and 42 Minutes",
        "page-number": "1,276",
        "wordcount": "468,023",
        "language": "French",
        "synopsis": "When d'Artagnan goes to Paris to become a Musketeer, he embarks on a swashbuckling adventure with the legendary Porthos, Athos, and Aramis. If they wish to trump the nefarious Cardinal Richelieu, it's got to be “all for one, one for all.",
        "publication-place": "France",
        "img-link": "https://m.media-amazon.com/images/S/compressed.photo.goodreads.com/books/1630475503i/7190.jpg"
    },

    {
        "id": 3,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "year": "1925",
        "genre": "Fiction",
        "rating": 3.93,
        "logline": "Set in the Jazz Age on Long Island, near New York City, the novel depicts first-person narrator Nick Carraway's interactions with Jay Gatsby, a mysterious millionaire obsessed with reuniting with his former lover, Daisy Buchanan.",
        "publisher": "Scribner",
        "maincharacters": "Jay Gatsby, Nick Carraway, Daisy Buchanan",
        "audiobook-duration": "4 Hours and 49 Minutes",
        "page-number": "180",
        "wordcount": "50,113",
        "language": "English",
        "synopsis": "The story of the mysteriously wealthy Jay Gatsby and his love for the beautiful Daisy Buchanan, of lavish parties on Long Island at a time when The New York Times noted “gin was the national drink and sex the national obsession,” it is an exquisitely crafted tale of America in the 1920s.",
        "publication-place": "United States",
        "img-link": "https://m.media-amazon.com/images/S/compressed.photo.goodreads.com/books/1650033243i/41733839.jpg"
    },

    {
        "id": 4,
        "title": "Fourth Wing",
        "author": "Rebecca Yarros",
        "year": "2023",
        "genre": "New Adult Fiction",
        "rating": 4.56,
        "logline": "Following the journey of Violet Sorrengail, who is forced by her mother, General Sorrengail, to join the Basgiath War College and become a dragon rider in the kingdom of Navarre.",
        "publisher": "Entangled: Red Tower Books",
        "maincharacters": "Violet Sorrengail, Lilith Sorrengail, Jack Barlowe",
        "audiobook-duration": "22 Hours and 2 Minutes",
        "page-number": "517",
        "wordcount": "207,841",
        "language": "English",
        "synopsis": "Twenty-year-old Violet Sorrengail was supposed to enter the Scribe Quadrant, living a quiet life among books and history. Now, the commanding general―also known as her tough-as-talons mother―has ordered Violet to join the hundreds of candidates striving to become the elite of Navarre: dragon riders.",
        "publication-place": "United States",
        "img-link": "https://m.media-amazon.com/images/S/compressed.photo.goodreads.com/books/1761312598i/61431922.jpg"
    },

    {
        "id": 5,
        "title": "Little Women",
        "author": "Louisa May Alcott",
        "year": "1868",
        "genre": "Fiction",
        "rating": 4.3,
        "logline": "A coming-of-age story of four sisters detailing their passage from childhood to womanhood.",
        "publisher": "Signet Classics",
        "maincharacters": "Josephine \"Jo\" March, Margaret \"Meg\" March, Elizabeth \"Beth\" March, Amy Curtis March, Marmee March",
        "audiobook-duration": "20 Hours and 59 Minutes",
        "page-number": "449",
        "wordcount": "198,799",
        "language": "English",
        "synopsis": "Generations of readers young and old, male and female, have fallen in love with the March sisters of Louisa May Alcott's most popular and enduring novel, Little Women. Here are talented tomboy and author-to-be Jo, tragically frail Beth, beautiful Meg, and romantic, spoiled Amy, united in their devotion to each other and their struggles to survive in New England during the Civil War.",
        "publication-place": "United States",
        "img-link": "https://m.media-amazon.com/images/S/compressed.photo.goodreads.com/books/1562690475i/1934.jpg"
    },

    {
        "id": 6,
        "title": "Lord of the Flies",
        "author": "William Golding",
        "year": "1954",
        "genre": "Dystopia",
        "rating": 3.7,
        "logline": "A novel about a group of boys stranded on an uninhabited island.",
        "publisher": "Faber and Faber",
        "maincharacters": "Ralph, Jack, The Lord of the Flies",
        "audiobook-duration": "6 Hours and 35 Minutes",
        "page-number": "182",
        "wordcount": "63,911",
        "language": "English",
        "synopsis": "At the dawn of the next world war, a plane crashes on an uncharted island, stranding a group of schoolboys. At first, with no adult supervision, their freedom is something to celebrate; this far from civilization the boys can do anything they want. Anything. They attempt to forge their own society, failing, however, in the face of terror, sin and evil. And as order collapses, as strange howls echo in the night, as terror begins its reign, the hope of adventure seems as far from reality as the hope of being rescued. Labeled a parable, an allegory, a myth, a morality tale, a parody, a political treatise, even a vision of the apocalypse, Lord of the Flies is perhaps our most memorable novel about \"the end of innocence, the darkness of man's heart.\"",
        "publication-place": "United Kingdom",
        "img-link": "https://m.media-amazon.com/images/S/compressed.photo.goodreads.com/books/1507895014i/7627.jpg"
    },

    {
        "id": 7,
        "title": "The Fellowship of the Ring",
        "author": "J.R.R. Tolkien",
        "year": "1954",
        "genre": "Fantasy",
        "rating": 4.41,
        "logline": "In a sleepy village in the Shire, young Frodo Baggins finds himself faced with an immense task, as his elderly cousin Bilbo entrusts the Ring to his care. Frodo must leave his home and make a perilous journey across Middle-earth to the Cracks of Doom, there to destroy the Ring and foil the Dark Lord in his evil purpose.",
        "publisher": "Ballantine Books",
        "maincharacters": "Frodo Baggins, Gnadalf, Aragorn",
        "audiobook-duration": "22 Hours and 38 Minutes",
        "page-number": "432",
        "wordcount": "209,282",
        "language": "English",
        "synopsis": "Sauron, the Dark Lord, has gathered to him all the Rings of Power - the means by which he intends to rule Middle-earth. All he lacks in his plans for dominion is the One Ring - the ring that rules them all - which has fallen into the hands of the hobbit, Bilbo Baggins.",
        "publication-place": "United Kingdom",
        "img-link": "https://m.media-amazon.com/images/S/compressed.photo.goodreads.com/books/1486871542i/3263607.jpg"
    },

    {
        "id": 8,
        "title": "Harry Potter and the Chamber of Secrets",
        "author": "J. K. Rowling",
        "year": "1998",
        "genre": "Fantasy",
        "rating": 4.43,
        "logline": "In Harry's second year at Hogwarts, fresh torments and horrors arise, but then the real trouble begins - someone is turning Hogwarts students to stone. Could it be Draco Malfoy, a more poisonous rival than ever? Could it possibly be Hagrid, whose mysterious past is finally told? Or could it be the one everyone at Hogwarts most suspects… Harry Potter himself!",
        "publisher": "Bloomsbury",
        "maincharacters": "Harry Potter, Ron Weasly, Hermione Granger, Ginny Weasley",
        "audiobook-duration": "9 Hours and 37 Minutes",
        "page-number": "341",
        "wordcount": "84,127",
        "language": "English",
        "synopsis": "During the school year, Harry hears a strange voice emanating from the castle walls. Argus Filch's cat is found magically immobilised, along with a warning scrawled on the wall: \"The Chamber of Secrets has been opened. Enemies of the heir, beware\". Harry learns that the Chamber supposedly houses a monster that attacks Muggle-born students, and which only the Heir of Slytherin can control. During a Quidditch match, a rogue Bludger strikes Harry, breaking his arm. Professor Lockhart botches an attempt to mend the injury, which sends Harry to the hospital wing. Dobby visits Harry and reveals that he jinxed the Bludger and sealed the portal at King's Cross. He also tells Harry that house-elves are bound to serve a master, and cannot be freed unless their master gives them clothing.",
        "publication-place": "United Kingdom",
        "img-link": "https://m.media-amazon.com/images/S/compressed.photo.goodreads.com/books/1553352368i/224912.jpg"
    },

    {
        "id": 9,
        "title": "A Game of Thrones",
        "author": "George R. R. Martin",
        "year": "1996",
        "genre": "Hystorical Fantasy",
        "rating": 4.45,
        "logline": " In the Seven Kingdoms of Westeros, House Stark and House Lannister influence the political fate of the continent.",
        "publisher": "Bantam Spectra and HarperCollins Voyager",
        "maincharacters": "Daenerys Tagarian, Sansa Stark, Jon Snow, Arya Stark, Tyrion Lannister",
        "audiobook-duration": "33 Hours and 46 Minutes",
        "page-number": "835",
        "wordcount": "325,781",
        "language": "English",
        "synopsis": "Sweeping from a harsh land of cold to a summertime kingdom of epicurean plenty, A Game of Thrones tells a tale of lords and ladies, soldiers and sorcerers, assassins and bastards, who come together in a time of grim omens. Here an enigmatic band of warriors bear swords of no human metal; a tribe of fierce wildlings carry men off into madness; a cruel young dragon prince barters his sister to win back his throne; a child is lost in the twilight between life and death; and a determined woman undertakes a treacherous journey to protect all she holds dear. Amid plots and counter-plots, tragedy and betrayal, victory and terror, allies and enemies, the fate of the Starks hangs perilously in the balance, as each side endeavors to win that deadliest of conflicts: the game of thrones.",
        "publication-place": "United Kingdom and United States",
        "img-link": "https://m.media-amazon.com/images/S/compressed.photo.goodreads.com/books/1562726234i/13496.jpg"
    },

    {
        "id": 10,
        "title": "Wuthering Heights",
        "author": "Emily Brontë",
        "year": "1847",
        "genre": "Tragedy",
        "rating": 3.89,
        "logline": "Driven by themes of love, possession, revenge, and reconciliation, the novel is influenced by Romanticism and Gothic fiction.",
        "publisher": "Penguin Classics",
        "maincharacters": "Heathcliff, Catherine Earnshaw, Edgar Linton, Ellen (Nelly) Dean",
        "audiobook-duration": "12 Hours and 32 Minutes",
        "page-number": "359",
        "wordcount": "114,605",
        "language": "English",
        "synopsis": "Lockwood, the new tenant of Thrushcross Grange, situated on the bleak Yorkshire moors, is forced to seek shelter one night at Wuthering Heights, the home of his landlord. There he discovers the history of the tempestuous events that took place years before. What unfolds is the tale of the intense love between Heathcliff and Catherine Earnshaw. Catherine, forced to choose between passionate, tortured Heathcliff and gentle, well-bred Edgar Linton, surrenders to the expectations of her class. As Heathcliff's bitterness and vengeance at his betrayal is visited upon the next generation, their innocent heirs must struggle to escape the legacy of the past.",
        "publication-place": "United Kingdom",
        "img-link": "https://m.media-amazon.com/images/S/compressed.photo.goodreads.com/books/1478641029i/32929156.jpg"
    },

    {
        "id": 11,
        "title": "The Awakening",
        "author": "Caroline Peckham",
        "year": "2019",
        "genre": "Romantasy",
        "rating": 3.82,
        "logline": "Two orphaned human-raised twin sisters discover they are Fae princesses and must survive a brutal magical boarding school ruled by hostile heirs to the throne.",
        "publisher": "Dark Ink Publishing",
        "maincharacters": "Darcy Vega, Tory Vega",
        "audiobook-duration": "12 Hours and 10 Minutes",
        "page-number": "436",
        "wordcount": "112,437",
        "language": "English",
        "synopsis": "The school they've sent me to is both dangerous as sh*t and one helluva party. Vampires bite weaker students in the corridors, the Werewolf pack has orgies in the Wailing Wood at every full moon and don't even get me started on the dark and twisted ways the Sirens use their powers on people's emotions, or how my sinfully tempting Cardinal Magic teacher hosts detentions that leave people needing therapy.",
        "publication-place": "United States",
        "img-link": "https://m.media-amazon.com/images/S/compressed.photo.goodreads.com/books/1560277389i/46261182.jpg"
    },

    {
        "id": 12,
        "title": "One of Us Is Lying",
        "author": "Karen M. McManus",
        "year": "2017",
        "genre": "Mystery Thriller",
        "rating": 3.9,
        "logline": "Before the end of detention Simon's dead, and according to investigators, his death wasn't an accident. On Monday, he died, but on Tuesday, he'd planned to post juicy reveals about all four of his high-profile classmates, which makes all four of them suspects in his murder. Or are they the perfect patsies for a killer who's still on the loose?",
        "publisher": "Delacorte Press",
        "maincharacters": "Bronwyn Rojas, Nathaniel \"Nate\" Macauley, Adelaide \"Addy\" Prentiss, Cooper Clay",
        "audiobook-duration": "1 Hour and 7 Minutes",
        "page-number": "170",
        "wordcount": "56,642",
        "language": "Classical Chinese",
        "synopsis": "Pay close attention and you might solve this.\nOn Monday afternoon, five students at Bayview High walk into detention.\nBronwyn, the brain, is Yale-bound and never breaks a rule.\nAddy, the beauty, is the picture-perfect homecoming princess.\nNate, the criminal, is already on probation for dealing.\nCooper, the athlete, is the all-star baseball pitcher.\nAnd Simon, the outcast, is the creator of Bayview High's notorious gossip app.\n\nOnly, Simon never makes it out of that classroom. Before the end of detention Simon's dead. And according to investigators, his death wasn't an accident. On Monday, he died. But on Tuesday, he'd planned to post juicy reveals about all four of his high-profile classmates, which makes all four of them suspects in his murder. Or are they the perfect patsies for a killer who's still on the loose?\n\nEveryone has secrets, right? What really matters is how far you would go to protect them.",
        "publication-place": "China",
        "img-link": "https://m.media-amazon.com/images/S/compressed.photo.goodreads.com/books/1632078539i/58679358.jpg"
    },

    {
        "id": 13,
        "title": "The Hunger Games",
        "author": "Suzanne Collins",
        "year": 2008,
        "genre": "Adventure",
        "rating": 4.35,
        "logline": "Winning means fame and fortune. Losing means certain death. The Hunger Games have begun. . . .",
        "publisher": "Scholastic Press",
        "maincharacters": "Katniss Everdeen, Peeta Mellark, Gale Hawthorne, Haymitch Abernathy, Primrose Everdeen",
        "audiobook-duration": "10 Hours and 35 Minutes",
        "page-number": "374",
        "wordcount": "59,690",
        "language": "English", 
        "synopsis": "In the ruins of a place once known as North America lies the nation of Panem, a shining Capitol surrounded by twelve outlying districts. The Capitol is harsh and cruel and keeps the districts in line by forcing them all to send one boy and one girl between the ages of twelve and eighteen to participate in the annual Hunger Games, a fight to the death on live TV. Sixteen-year-old Katniss Everdeen regards it as a death sentence when she steps forward to take her sister's place in the Games. But Katniss has been close to dead before-and survival, for her, is second nature. Without really meaning to, she becomes a contender. But if she is to win, she will have to start making choices that weigh survival against humanity and life against love.",
        "publication-place": "United States",
        "img-link": "https://m.media-amazon.com/images/S/compressed.photo.goodreads.com/books/1586722975i/2767052.jpg"
    },

    {
        "id": 14,
        "title": "Twisted Hate",
        "author": "Ana Huang",
        "year": 2022,
        "genre": "Romance",
        "rating": 3.93,
        "logline": "A cocky medical resident and his best friend's stubborn law-student nemesis who enter a no-strings-attached arrangement, only to have their fiery mutual hatred threatened by undeniable attraction and dark pasts.",
        "publisher": "Bloom",
        "maincharacters": "Jules Ambrose and Josh Chen",
        "audiobook-duration": "15 Hours",
        "page-number": "500",
        "wordcount": "137,340",
        "language": "English", 
        "synopsis": "He hates her… almost as much as he wants her.\nGorgeous, cocky, and fast on his way to becoming a hotshot doctor, Josh Chen has never met a woman he couldn't charm—except for Jules f**king Ambrose.\nThe beautiful redhead has been a thorn in his side since they met, but she also consumes his thoughts in a way no woman ever has.\nWhen their animosity explodes into one unforgettable night, he proposes a solution that'll get her out of his system once and for all: an enemies with benefits arrangement with simple rules.\nNo jealousy.\nNo strings attached.\nAnd absolutely no falling in love.\nOutgoing and ambitious, Jules Ambrose is a former party girl who's focused on one thing: passing the attorney's bar exam.\nThe last thing she needs is to get involved with a doctor who puts the SUFFER in insufferable…no matter how good-looking he is.\nBut the more she gets to know him, the more she realizes there's more than meets the eye to the man she's hated for so long. Her best friend's brother.\nHer nemesis.\nAnd her only salvation.\nTheirs is a match made in hell, and when the demons from their past catch up with them, they're faced with truths that could either save them… or destroy everything they've worked for.",
        "publication-place": "United States, United Kingdom, and Australia",
        "img-link": "https://m.media-amazon.com/images/S/compressed.photo.goodreads.com/books/1661221520i/62056935.jpg"
    },

    {
        "id": 15,
        "title": "Love on the Brain",
        "author": "Ali Hazelwood",
        "year": 2022,
        "genre": "Contemporary Romance",
        "rating": 3.9,
        "logline": "When a brilliant neuroscientist lands her dream NASA project, she must co-lead it with her fierce graduate school archenemy, only to discover that professional tension might just spark an explosive romance.",
        "publisher": "Sphere",
        "maincharacters": "Bee Königswasser and Levi Ward",
        "audiobook-duration": "11 Hours and 7 Minutes",
        "page-number": "368",
        "wordcount": "98,316",
        "language": "English", 
        "synopsis": "Bee Königswasser lives by a simple code: What would Marie Curie do? If NASA offered her the lead on a neuroengineering project - a literal dream come true - Marie would accept without hesitation. Duh. But the mother of modern physics never had to co-lead with Levi Ward.\nSure, Levi is attractive in a tall, dark, and piercing-eyes kind of way. But Levi made his feelings toward Bee very clear in grad school - archenemies work best employed in their own galaxies far, far away.\nBut when her equipment starts to go missing and the staff ignore her, Bee could swear she sees Levi softening into an ally, backing her plays, seconding her ideas... devouring her with those eyes. The possibilities have all her neurons firing.\nBut when it comes time to actually make a move and put her heart on the line, there's only one question that matters: What will Bee Königswasser do?",
        "publication-place": "United States",
        "img-link": "https://m.media-amazon.com/images/S/compressed.photo.goodreads.com/books/1657897729i/59571699.jpg"
    },

    {
        "id": 16,
        "title": "The Hating Game",
        "author": "Sally Thorne",
        "year": 2016,
        "genre": "Contemporary Romance",
        "audiobook-duration": "12 Hours and 18 Minutes",
        "rating": 3.85,
        "logline": "Trapped in a shared office, two rival executive assistants at a publishing company must compete for a major promotion, but their intense mutual animosity turns to unexpected chemistry when a high-stakes battle of wills crosses the line into desire.",
        "publisher": "William Morrow Paperbacks",
        "maincharacters": "Bee Königswasser and Levi Ward",
        "page-number": "365",
        "wordcount": "107,305",
        "language": "English", 
        "synopsis": "Nemesis (n.)\n1) An opponent or rival whom a person cannot best or overcome;\n2) A person's undoing;\n3) Joshua Templeman.\nLucy Hutton and Joshua Templeman hate each other. Not dislike. Not begrudgingly tolerate. Hate. And they have no problem displaying their feelings through a series of ritualistic passive aggressive maneuvers as they sit across from each other, executive assistants to co-CEOs of a publishing company. Lucy can't understand Joshua's joyless, uptight, meticulous approach to his job. Joshua is clearly baffled by Lucy's overly bright clothes, quirkiness, and Pollyanna attitude.\nNow up for the same promotion, their battle of wills has come to a head and Lucy refuses to back down when their latest game could cost her her dream job…But the tension between Lucy and Joshua has also reached its boiling point, and Lucy is discovering that maybe she doesn't hate Joshua. And maybe, he doesn't hate her either. Or maybe this is just another game.",
        "publication-place": "United States",
        "img-link": "https://m.media-amazon.com/images/S/compressed.photo.goodreads.com/books/1481566824i/27213238.jpg"
    },

    {
        "id": 17,
        "title": "Archer's Voice",
        "author": "Mia Sheridan",
        "year": 2014,
        "genre": "Contemporary Romance",
        "rating": 4.16,
        "logline": "When a traumatized woman seeking peace in a small Maine town collides with a reclusive, mute man harboring his own secret agony, they must rely on an unspoken, transformative love to break their respective chains and heal their pasts.",
        "publisher": "Forever",
        "maincharacters": "Archer Hale, Bree Prescott, Travis Hale, Victoria Hale, and Jeffrey Perkins",
        "audiobook-duration": "11 Hours and 50 Minutes",
        "page-number": "377",
        "wordcount": "111,760",
        "language": "English", 
        "synopsis": "Archer's Voice is the story of a woman chained to the memory of one horrifying night and the man whose love is the key to her freedom. It is the story of a silent man who lives with an excruciating wound and the woman who helps him find his voice. It is the story of suffering, fate, and the transformative power of love.",
        "publication-place": "United States",
        "img-link": "https://m.media-amazon.com/images/S/compressed.photo.goodreads.com/books/1656593818i/32822135.jpg"
    },

    {
        "id": 18,
        "title": "Pack Up the Moon",
        "author": "Kristan Higgins",
        "year": 2021,
        "genre": "Romance",
        "rating": 4.15,
        "logline": "When a devoted husband loses his terminally ill wife, he must navigate his first year of grief using a series of monthly letters she left behind to guide him back toward a life of love and laughter.",
        "publisher": "Berkley",
        "maincharacters": "Joshua Park, Lauren Park, and Sarah Fitzpatrick",
        "audiobook-duration": "13 Hours and 37 Minutes",
        "page-number": "480",
        "wordcount": "123,420",
        "language": "English", 
        "synopsis": "Joshua and Lauren are the perfect couple. Newly married, they're wildly in love, each on a successful and rewarding career path. Then Lauren is diagnosed with a terminal illness.\nAs Lauren's disease progresses, Joshua struggles to make the most of the time he has left with his wife and to come to terms with his future--a future without the only woman he's ever loved. He's so consumed with finding a way to avoid the inevitable ending that he never imagines his life after Lauren.\nBut Lauren has a plan to keep her husband moving forward. A plan hidden in the letters she leaves him. In those letters, one for every month in the year after her death, Lauren leads Joshua on a journey through pain, anger, and denial. It's a journey that will take Joshua from his attempt at a dinner party for family and friends to getting rid of their bed...from a visit with a psychic medium to a kiss with a woman who isn't Lauren. As his grief makes room for laughter and new relationships, Joshua learns Lauren's most valuable lesson: The path to happiness doesn't follow a straight line.",
        "publication-place": "United States",
        "img-link": "https://m.media-amazon.com/images/S/compressed.photo.goodreads.com/books/1605447045i/55445159.jpg"
    },

    {
        "id": 19,
        "title": "A Good Girl's Guide to Murder",
        "author": "Holly Jackson",
        "year": 2019,
        "genre": "Mystery",
        "rating": 4.28,
        "logline": "Pippa \"Pip\" Fitz-Amobi investigates the murder of popular student Andrea \"Andie\" Bell and the suicide of the supposed perpetrator Salil \"Sal\" Singh under the guise of a school project. ",
        "publisher": "Electric Monkey",
        "maincharacters": "Pippa \"Pip\" Fitz-Amobi, Ravi Singh, and Cara Ward",
        "audiobook-duration": "10 Hours and 53 Minutes",
        "page-number": "433",
        "wordcount": "87,763",
        "language": "English", 
        "synopsis": "The case is closed. Five years ago, schoolgirl Andie Bell was murdered by Sal Singh. The police know he did it. Everyone in town knows he did it.\nBut having grown up in the same small town that was consumed by the crime, Pippa Fitz-Amobi isn't so sure. When she chooses the case as the topic for her final project, she starts to uncover secrets that someone in town desperately wants to stay hidden. And if the real killer is still out there, how far will they go to keep Pip from the truth…?",
        "publication-place": "United Kingdom and United States",
        "img-link": "https://m.media-amazon.com/images/S/compressed.photo.goodreads.com/books/1545494980i/40916679.jpg"
    },

    {
        "id": 20,
        "title": "The Silent Patient",
        "author": "Alex Michaelides",
        "year": 2019,
        "genre": "Psychological Thriller",
        "rating": 4.0,
        "logline": "In an attempt to fix and understand himself, Theo takes a degree in psychology and starts working as a therapist and finds the love of his life in Kathy, an American actress who lives in London, Theo feels safe and his relationship means everything to him but it becomes increasingly clear that Kathy is traitorous.",
        "publisher": "Celadon Books",
        "maincharacters": "Theo Faber, Alicia Berenson, and Kathy",
        "audiobook-duration": "8 Hours and 33 Minutes",
        "page-number": "336",
        "wordcount": "73,154",
        "language": "English", 
        "synopsis": "Alicia Berenson's life is seemingly perfect. A famous painter married to an in-demand fashion photographer, she lives in a grand house with big windows overlooking a park in one of London's most desirable areas. One evening her husband Gabriel returns home late from a fashion shoot, and Alicia shoots him five times in the face, and then never speaks another word.\nAlicia's refusal to talk, or give any kind of explanation, turns a domestic tragedy into something far grander, a mystery that captures the public imagination and casts Alicia into notoriety. The price of her art skyrockets, and she, the silent patient, is hidden away from the tabloids and spotlight at the Grove, a secure forensic unit in North London.\nTheo Faber is a criminal psychotherapist who has waited a long time for the opportunity to work with Alicia. His determination to get her to talk and unravel the mystery of why she shot her husband takes him down a twisting path into his own motivations—a search for the truth that threatens to consume him...",
        "publication-place": "United Kingdom",
        "img-link": "https://m.media-amazon.com/images/S/compressed.photo.goodreads.com/books/1668782119i/40097951.jpg"
    }

]

# HOME
@app.get("/")
def home():

    return {
        "message": "Welcome to the Simple Book API!",
        "endpoints": [
            "/books",
            "/books/{id}",
            "/books/search"
        ]
    }


# GET ALL BOOKS
@app.get("/books")
def get_books():

    return {
        "count": len(books),
        "books": books
    }

# SEARCH BOOKS
@app.get("/books/search")
def search_books( q: str = Query(..., min_length=1)):
    q = q.lower()
    results = []
    for book in books:
        searchable_text = (
            f"{book['title']} "
            f"{book['author']} "
            f"{book['genre']}"
            f"{book['year']}"
            f"{book['language']}"
            f"{book['publisher']}"
            f"{book['publication-place']}"
        ).lower()

        if q in searchable_text:
            results.append(book)

    return {
        "query": q,
        "count": len(results),
        "results": results
    }

# GET ONE BOOK
@app.get("/books/{book_id}")
def get_book(book_id: int):

    for book in books:

        if book["id"] == book_id:
            return book

    raise HTTPException(
        status_code=404,
        detail="Book not found."
    )
