from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional

load_dotenv()
chatLLM = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=1.6)

# Decide the schema - how you want the result to be.
class reviewSummary(TypedDict) :
    brand:Annotated[str, 'name of the brand']
    model:Annotated[str, 'name of the model from that brand']
    recommended:Annotated[str, 'is it recommeded or no - Only answer with Yes or No with % confidence, Not True/false.']
    sentiment:str
    battery_backup:Annotated[str,'How many hours,days does the model run on a single charge.']
    key_themes:Annotated[list[str], 'List down all the key themes.']
    pros:Annotated[Optional[list[str]], 'list down all the pros of the model & chosing this model']
    cons:Annotated[Optional[list[str]], 'list down all the cons of the model & chosing this model']

# call the with_structured_output with class.
new_summary = chatLLM.with_structured_output(reviewSummary)

prompt = """I’ve been using the NovaTech X12 Pro for about three weeks now, and overall it’s a really solid phone for the price. The first thing that stood out to me was the display — the 120Hz AMOLED panel looks fantastic. Colors are vibrant, scrolling feels super smooth, and watching Netflix or YouTube on it is genuinely enjoyable. Brightness is also good enough outdoors, which I appreciated while traveling.

Battery life is probably the best feature here. With moderate to heavy usage, I consistently got through an entire day with around 20–25% left. On lighter days, it even lasted close to two days. The 80W fast charging is crazy fast too — around 35–40 minutes for a full charge.

Performance-wise, the phone handles almost everything without issues. Apps open quickly, multitasking is smooth, and games like BGMI and Call of Duty Mobile run at high settings comfortably. I didn’t notice major heating except during long gaming sessions.

The cameras are good but not amazing. In daylight, photos come out sharp with nice colors, but low-light performance is inconsistent. Night mode helps a bit, but details still get soft and noisy compared to flagship phones. The selfie camera is decent for social media and video calls though.

Now for the downsides — the software experience could definitely be cleaner. There are too many pre-installed apps, and some of them keep sending notifications unless you disable them manually. The phone is also slightly bulky and heavy, so one-handed use isn’t very comfortable.

Build quality feels premium thanks to the metal frame and glass back, and the IP68 water resistance is a nice bonus in this price range.

So, should you buy it? I’d say yes if your priorities are battery life, display quality, and performance. It’s especially good for students, casual gamers, and people who consume a lot of media. But if camera quality is your top priority, especially night photography, there are better options available.
"""
result = new_summary.invoke(prompt)
print('Pros--------',result['pros'])
print('cons',result['cons'])
print('key_themes',result['key_themes'])

