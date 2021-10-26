{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "f4edd32a-666b-48ba-9086-3be033f58788",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "min value element :  0.0\n",
      "max value element :  9.0\n"
     ]
    }
   ],
   "source": [
    "#For other numeric types besides lat and lon, what are the min and max values?\n",
    "import csv,time,datetime\n",
    "\n",
    "fn='C:/Users/yasha/OneDrive/Documents/Yahsaswini/Big data procs/Week-4 Homework/trip_data_12.csv'\n",
    "f= open(fn,'r')\n",
    "reader = csv.reader(f)\n",
    "\n",
    "maxpassenger_count = []\n",
    "minpassenger_count = []\n",
    "\n",
    "n=0\n",
    "for row in reader:\n",
    "    if n>0:\n",
    "            try:\n",
    "                maxpassenger_count.append(float(row[7]))\n",
    "                minpassenger_count.append(float(row[7]))\n",
    "            except ValueError:\n",
    "                print (\"error\",\"on line\",row)\n",
    "    n +=1\n",
    "       \n",
    "print (\"min value of passeneger count : \", min(minpassenger_count))\n",
    "print (\"max value of passeneger count : \", max(maxpassenger_count))\n",
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
    "print (\"max value of trip distance : \", max(maxtrip_distance))\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "628afb11-665f-4fcf-98e0-633a66e7ed15",
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
