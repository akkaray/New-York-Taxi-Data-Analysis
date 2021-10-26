{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "07f70826-16f8-4854-8ae8-8b272d85f505",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'00': 579445, '02': 319486, '04': 170362, '06': 274264, '08': 586809, '09': 626675, '10': 646517, '01': 431891, '07': 0, '12': 716597, '13': 712226, '14': 728487, '15': 684458, '11': 684616, '16': 552019, '17': 668861, '03': 230655, '05': 140360, '18': 809795, '20': 810965, '21': 804841, '19': 842699, '22': 785933, '23': 704158, 'pickup_datetime': 1}\n"
     ]
    }
   ],
   "source": [
    "Create a chart which shows the average number of passengers each hour of the day. (X axis should have 24 hours)\n",
    "\n",
    "import csv,time,datetime\n",
    "\n",
    "fn='Subsetfile.csv'\n",
    "f= open(fn,'r')\n",
    "reader = csv.reader(f)\n",
    "\n",
    "n=0\n",
    "hhist = {}\n",
    "for row in reader:\n",
    "    if n>0:\n",
    "        \n",
    "        hr = row[5].split(\" \")[1].split(\":\")[0]\n",
    "    \n",
    "        if hr in hhist.keys():\n",
    "            hhist[hr] += 1\n",
    "        else:\n",
    "            hhist[hr] = 1\n",
    "    n+=1\n",
    "for i in hhist.keys():\n",
    "    hhist[hr] = hhist[hr]//31\n",
    "print(hhist)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e79ae20a-8ca2-4ef8-b6ff-82f6765f155f",
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
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
