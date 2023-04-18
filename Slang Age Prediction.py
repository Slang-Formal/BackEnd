{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "3777300e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Age: 18-29\n"
     ]
    }
   ],
   "source": [
    "test_string = \"bro he told me that he wasn't a simp but i think that's cap\"\n",
    "\n",
    "low_dict = {\"ded\", \"spoopy\",\"blankie\", \"tummyache\", \"tummy ache\", \"ouchie\", \"sippy cup\", \"potty\",\"binky\", \"boo boo\", \"boo-boo\", \"tummy\", \"yucky\", \"no no\", \"no-no\", \"blankey\", \"wawa\", \"nigh-nigh\", \"nigh nigh\", \"nini\", \"nuggies\",\"uwu\", \"dank\",\"catch feelings\", \"caught feelings\", \"normie\", \"moots\", \"baller\", \"sigma\", \"alpha\", \"fleek\", \"bff\", \"stan\", \"noob\", \"bae\", \"simp\", \"simping\", \"sus\", \"squad\", \"shook\", \"salty\", \"AF\", \"lit\", \"unalive\", \"clutch\", \"boi\", \"based\", \"rizz\", \"shading\", \"shade\", \"weaboo\"}\n",
    "mid_dict = { \"goofy\", \"GOAT\", \"gucci\", \"yeet\", \"mood\", \"lit\", \"stan\", \"clout\", \"vibe\", \"vibes\", \"FOMO\",\"IRL\", \"TBH\", \"salty\", \"savage\", \"periodt\",\"bruh\", \"bro\", \"dude\", \"chad\", \"zoomies\", \"L+ratio\", \"L + ratio\", \"caucacity\", \"lovebomb\", \"tripping\", \"trippin\", \"crunk\", \"flex\", \"cap\", \"bop\", \"chillax\", \"periodt\",\"bruh\", \"yassify\", \"slay\", \"highk\" \"highkey\", \"lowkey\",\"boomer\", \"lowk\", \"ONG\", \"go off\", \"tea\", \"flex\", \"ghosted\", \"ghosting\", \"woke\", \"bro\", \"fam\", \"glow up\", \"cancel culture\", \"eboy\", \"egirl\",\"e-boy\", \"e-girl\", \"ghosting\", \"boujee\", \"finna\", \"cheugy\", \"smexy\", \"clapback\", \"snacc\", \"full send\", \"clutch\", \"ratchet\", \"brazy\", \"deadass\", \"based\", \"quid pro quo\", \"bars\", \"bih\", \"bussin\", \"cake\", \"dope\", \"drip\", \"facts\", \"finsta\", \"fire\", \"gas\", \"gtg\", \"hits different\", \"hits diff\", \"turnt\", \"LOL\", \"LMAO\", \"mid\",\"xtra\", \"woe is me\", \"mami\", \"fav\", \"netflix and chill\", \"plug\", \"rizz\", \"smash\", \"zaddy\",\"yuge\",\"poppin\", \"oppa\", \"thirsty\", \"snatched\", \"extra\", \"adulting\", \"side eye\", \"ride or die\"}\n",
    "high_dict = {\"golly\", \"darn\",\"fuddy-duddy\", \"hooey\", \"cat's pajamas\", \"rad\", \"righteous\", \"bee's knees\", \"foxy\", \"cool cat\", \"gee whiz\", \"gobbledygook\", \"hooey\", \"jive\", \"sock hop\", \"whippersnapper\", \"juke joint\", \"ducky\", \"g-man\", \"saddle shoes\", \"groovy\", \"far out\", \"goofy\", \"cool beans\", \"bummer\", \"hippy\", \"peace\", \"hang loose\", \"right on\", \"hotsy-totsy\",\"tots\", \"rugrats\", \"mini-me's\", \"ankle-biters\", \"throuple\",\"bell end\", \"brigading\", \"brigade\", \"adorkable\", \"food coma\", \"iykyk\", \"sup\", \"yadda\", \"GOAT\",\"wassup\", \"diss\", \"newbie\", \"hangry\", \"buzzkill\", \"dibs\", \"quid pro quo\", \"ROFL\"}\n",
    "\n",
    "\n",
    "low = 0 # Ages under 18\n",
    "mid = 0 # Ages 18-29 \n",
    "high = 0 # Ages 30 and up\n",
    "\n",
    "def agePrediction(string):\n",
    "    text = string.split(\" \")\n",
    "    global low, mid, high\n",
    "    for word in text:\n",
    "        if word in low_dict:\n",
    "            low += 1\n",
    "        elif word in mid_dict:\n",
    "            mid += 1\n",
    "        elif word in high_dict:\n",
    "            high += 1\n",
    "        else:\n",
    "            pass\n",
    "        \n",
    "    if max(low, mid, high) == low:\n",
    "        return \"Age: under 18\"\n",
    "    elif max(low, mid, high) == mid:\n",
    "        return \"Age: 18-29\"\n",
    "    elif max(low, mid, high) == high:\n",
    "        return \"Age: 30 and up\"\n",
    "    else:\n",
    "        return \"All Ages\"\n",
    "    \n",
    "    \n",
    "        \n",
    "print(agePrediction(test_string))\n",
    "    \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fae72d17",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}