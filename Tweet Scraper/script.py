import twint
import nest_asyncio
nest_asyncio.apply()

def tweets(name):
    t = twint.Config()
    t.Username = name
    t.Store_object = True
    t.Limit = 15
    t.Store_csv = True
    t.Output = name + ".csv"
    twint.run.Search(t)

tweets("curiousharish")
tweets("Shreyans_23")
