{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "b693a5f1-240f-4878-b363-3e9a406496d8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "min value of trip distance :  0.0\n",
      "max value of trip distance :  100.0\n"
     ]
    }
   ],
   "source": [
    "#Repeat step 9 with the reduced dataset and compare the two charts\n",
    "import csv,time,datetime\n",
    "\n",
    "fn='Subsetfile.csv'\n",
    "f= open(fn,'r')\n",
    "reader = csv.reader(f)\n",
    "\n",
    "maxtrip_secs = []\n",
    "mintrip_secs = []\n",
    "\n",
    "n=0\n",
    "for row in reader:\n",
    "    if n>0:\n",
    "            try:\n",
    "                maxtrip_secs.append(float(row[8]))\n",
    "                mintrip_secs.append(float(row[8]))\n",
    "            except ValueError:\n",
    "                print (\"error\",\"on line\",row)\n",
    "    n +=1\n",
    "       \n",
    "print (\"min value of trip in secs: \", min(mintrip_secs))\n",
    "print (\"max value oftrip in secs: \", max(maxtrip_secs))\n",
    "\n",
    "maxtrip_distance= []\n",
    "mintrip_distance = []\n",
    "\n",
    "n=0\n",
    "for row in reader:\n",
    "    if n>0:\n",
    "            try:\n",
    "                maxtrip_distance.append(float(row[9]))\n",
    "                mintrip_distance.append(float(row[9]))\n",
    "                \n",
    "            except ValueError:\n",
    "                print (\"error\",\"on line\",row)\n",
    "    n +=1\n",
    "       \n",
    "print (\"min value of trip distance : \", min(mintrip_distance))\n",
    "print (\"max value of trip distance : \", max(maxtrip_distance))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6acbf8c2-6173-4455-bc0c-c44b7e6714cc",
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
