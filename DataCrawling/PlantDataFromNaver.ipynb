{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting seleniumNote: you may need to restart the kernel to use updated packages.\n",
      "  Using cached selenium-3.141.0-py2.py3-none-any.whl (904 kB)\n",
      "\n",
      "Requirement already satisfied: urllib3 in c:\\programdata\\anaconda3\\lib\\site-packages (from selenium) (1.25.8)\n",
      "Installing collected packages: selenium\n",
      "Successfully installed selenium-3.141.0\n"
     ]
    }
   ],
   "source": [
    "pip install selenium"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "from selenium import webdriver\n",
    "from selenium.webdriver.common.keys import Keys\n",
    "import time\n",
    "import bs4\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'webdriver' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-1-af0f7aeac58d>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      5\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      6\u001b[0m \u001b[0mkeyword\u001b[0m \u001b[1;33m=\u001b[0m \u001b[1;34m\"감귤\"\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 7\u001b[1;33m \u001b[0mdriver\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mwebdriver\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mChrome\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34mr'C:\\Users\\Yang\\Desktop\\chromedriver.exe'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      8\u001b[0m \u001b[0mdriver\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mget\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'https://search.shopping.naver.com/search/all.nhn?where=all&frm=NVSCTAB&query={}'\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mformat\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mkeyword\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'webdriver' is not defined"
     ]
    }
   ],
   "source": [
    "t_list = []\n",
    "n_list = []\n",
    "r_list = []\n",
    "p_list = []\n",
    "\n",
    "keyword = \"감귤\"\n",
    "driver = webdriver.Chrome(r'C:\\Users\\Yang\\Desktop\\chromedriver.exe')\n",
    "driver.get('https://search.shopping.naver.com/search/all.nhn?where=all&frm=NVSCTAB&query={}'.format(keyword))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "item_source = bs4.BeautifulSoup(driver.page_source, 'lxml')\n",
    "item_list = item_source.find_all('div', class_='info')\n",
    "\n",
    "for item in item_list[4:]:\n",
    "    title = item.find('a').text.replace('\\n', '')\n",
    "    price = item.find('span', class_='num').text\n",
    "    if item.find_all('a', class_='graph'):\n",
    "        review = item.find_all('a', class_='graph')[0].text\n",
    "        if len(item.find_all('a', class_='graph')) == 2:\n",
    "            buy_num = item.find_all('a', class_='graph')[1].text\n",
    "        else:\n",
    "            buy_num = '없음'\n",
    "            \n",
    "    t_list.append(title)\n",
    "    p_list.append(price)\n",
    "    r_list.append(review.replace('리뷰',''))\n",
    "    n_list.append(buy_num.replace('구매건수',''))\n",
    "    \n",
    "pd.DataFrame({'상품명':t_list, '가격':p_list, '리뷰수':r_list, '구매건수':n_list})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
