{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "1e6b896b-5bc6-4d3f-bbca-6c8cb2e8228f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'00': 578839, '02': 319145, '04': 170197, '06': 274000, '08': 586239, '09': 626087, '10': 645822, '01': 431452, '07': 0, '12': 715879, '13': 711522, '14': 727719, '15': 683750, '11': 683931, '16': 551464, '17': 668208, '03': 230387, '05': 140219, '18': 809013, '20': 810127, '21': 804089, '19': 841892, '22': 785152, '23': 703506}\n"
     ]
    }
   ],
   "source": [
    "#Create a chart which shows the average number of passengers each hour of the day. (X axis should have 24 hours)\n",
    "import csv,time,datetime\n",
    "\n",
    "fn='C:/Users/yasha/OneDrive/Documents/Yahsaswini/Big data procs/Week-4 Homework/trip_data_12.csv'\n",
    "f= open(fn,'r')\n",
    "reader = csv.reader(f)\n",
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
    "print(hhist)\n",
    "\n",
    "#Create a new CSV file which has only one out of every thousand rows.\n",
    "\n",
    "f2 = open('Subsetfile.csv','a')\n",
    "writer = csv.writer(f2,delimiter=',',lineterminator='\\n')\n",
    "n=0\n",
    "for row in reader:\n",
    "    if n % 1000 == 0:\n",
    "        writer.writerow(row)\n",
    "    n += 1\n",
    "\n",
    "\n",
    "f.close\n",
    "f2.close()\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a3a2b297-1720-4463-b341-fd8422134a7c",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bc695e4f-04bc-46dd-b608-60421da582ec",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6347a267-18e2-4ba6-b6ff-33687666aebb",
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
