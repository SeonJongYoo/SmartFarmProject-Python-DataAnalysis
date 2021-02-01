{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
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
   "execution_count": 57,
   "metadata": {},
   "outputs": [],
   "source": [
    "#pagenumber = 49  # 고급 채소 \n",
    "#52 일반 채소, 30 샐러드용,  27 쌈채소,  48 쌈채 도매가(박스), 26 향신료\n",
    "number = 1  # page수 처리하기!\n",
    "keyword='샐러리'\n",
    "driver = webdriver.Chrome(r'C:\\Users\\jobgs\\Desktop\\CONCAT_SMARTFARM_Project\\DataScience\\SMARTFARM_Project-DataAnalysis_Plant\\chromedriver.exe')\n",
    "#try:\n",
    "#driver.get('http://grfarm.co.kr/product/list.html?cate_no={0}&page={1}'.format(pagenumber, number))\n",
    "#driver.get('http://grfarm.co.kr/product/search.html?banner_action=&keyword={}'.format(keyword))\n",
    "#except KeyError:\n",
    "\n",
    "while True:    \n",
    "    #driver.get('http://grfarm.co.kr/product/list.html?cate_no={0}&page={1}'.format(pagenumber, number))\n",
    "    driver.get('http://grfarm.co.kr/product/search.html?banner_action=&keyword={0}&page={}'.format(keyword, number))\n",
    "    time.sleep(0.5)\n",
    "    number += 1\n",
    "\n",
    "    driver.execute_script(\"window.scrollTo(0, document.body.scrollHeight);\")\n",
    "    time.sleep(1)\n",
    "\n",
    "\n",
    "    item_source = bs4.BeautifulSoup(driver.page_source, 'lxml')\n",
    "    item_list = item_source.select('div.box_design3')\n",
    "\n",
    "    if not item_list:\n",
    "        break\n",
    "\n",
    "    else:\n",
    "        title_list = []\n",
    "        price_list = []\n",
    "\n",
    "        for item in item_list:\n",
    "            title = item.select_one('div.description.item_list > p > a').text.replace('\\n', '')\n",
    "            price = item.select_one('li.xans-record-').text.replace('\\n', '')\n",
    "            \n",
    "            title_list.append(title)\n",
    "            price_list.append(price)\n",
    "            \n",
    "        #print(title_list, price_list)\n",
    "        df = pd.DataFrame({'상품명':title_list, '가격':price_list})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'while True:    \\n    driver.get(\\'https://search.shopping.naver.com/search/all?frm=NVSHATC&origQuery={}&pagingIndex={}&pagingSize=80&productSet=total&query={}&sort=rel&timestamp=&viewType=list\\'.format(keyword, i, keyword))\\n    time.sleep(0.5)\\n    i += 1\\n\\n    driver.execute_script(\"window.scrollTo(0, document.body.scrollHeight);\")\\n    time.sleep(1)\\n\\n\\n    item_source = bs4.BeautifulSoup(driver.page_source, \\'lxml\\')\\n    item_list = item_source.select(\\'div.basicList_info_area__17Xyo\\')\\n\\n    if not item_list:\\n        break\\n\\n    else:\\n        for item in item_list:\\n            title = item.select_one(\\'a\\').text.replace(\\'\\n\\', \\'\\')\\n            price = item.select_one(\\'span.price_num__2WUXn\\').text\\n            ReviewAndBuy = item.select(\\'a.basicList_etc__2uAYO > em\\')\\n            try:\\n                review = ReviewAndBuy[0].text + \\'개\\'\\n            except IndexError:\\n                review = \\'없음\\'\\n\\n            try:\\n                buy = ReviewAndBuy[1].text + \\'개\\'\\n            except IndexError:\\n                buy = \\'없음\\'\\n\\n            title_list.append(title)\\n            price_list.append(price)\\n            review_list.append(review)\\n            buy_list.append(buy)\\n\\ndf = pd.DataFrame({\\'상품명\\':title_list, \\'가격\\':price_list, \\'리뷰수\\':review_list, \\'구매건수\\':buy_list})'"
      ]
     },
     "execution_count": 59,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'''while True:    \n",
    "    driver.get('https://search.shopping.naver.com/search/all?frm=NVSHATC&origQuery={}&pagingIndex={}&pagingSize=80&productSet=total&query={}&sort=rel&timestamp=&viewType=list'.format(keyword, i, keyword))\n",
    "    time.sleep(0.5)\n",
    "    i += 1\n",
    "\n",
    "    driver.execute_script(\"window.scrollTo(0, document.body.scrollHeight);\")\n",
    "    time.sleep(1)\n",
    "\n",
    "\n",
    "    item_source = bs4.BeautifulSoup(driver.page_source, 'lxml')\n",
    "    item_list = item_source.select('div.basicList_info_area__17Xyo')\n",
    "\n",
    "    if not item_list:\n",
    "        break\n",
    "\n",
    "    else:\n",
    "        for item in item_list:\n",
    "            title = item.select_one('a').text.replace('\\n', '')\n",
    "            price = item.select_one('span.price_num__2WUXn').text\n",
    "            ReviewAndBuy = item.select('a.basicList_etc__2uAYO > em')\n",
    "            try:\n",
    "                review = ReviewAndBuy[0].text + '개'\n",
    "            except IndexError:\n",
    "                review = '없음'\n",
    "\n",
    "            try:\n",
    "                buy = ReviewAndBuy[1].text + '개'\n",
    "            except IndexError:\n",
    "                buy = '없음'\n",
    "\n",
    "            title_list.append(title)\n",
    "            price_list.append(price)\n",
    "            review_list.append(review)\n",
    "            buy_list.append(buy)\n",
    "\n",
    "df = pd.DataFrame({'상품명':title_list, '가격':price_list, '리뷰수':review_list, '구매건수':buy_list})'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "title_list = []\n",
    "        price_list = []\n",
    "        status_list = []\n",
    "\n",
    "        for item in item_list:\n",
    "            title = item.select_one('div.description.item_list > p > a').text.replace('\\n', '')\n",
    "            price = item.select_one('li.xans-record-').text.replace('\\n', '')\n",
    "            status = item.select_one('div.pro_icon > img.icon_img')\n",
    "\n",
    "            title_list.append(title)\n",
    "            price_list.append(price)\n",
    "            if status is None:\n",
    "                sts = '판매중'\n",
    "            else:\n",
    "                sts = '품절'\n",
    "            status_list.append(sts)\n",
    "        #print(title_list, price_list, status_list)\n",
    "        df = pd.DataFrame({'상품명':title_list, '가격':price_list, '판매 상태':status_list})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "List is Empty!\n"
     ]
    }
   ],
   "source": [
    "time.sleep(3)\n",
    "driver.execute_script(\"window.scrollTo(0, document.body.scrollHeight);\")\n",
    "time.sleep(1)\n",
    "\n",
    "\n",
    "item_source = bs4.BeautifulSoup(driver.page_source, 'lxml')\n",
    "item_list = item_source.select('div.box_design3')\n",
    "if not item_list:\n",
    "    print('List is Empty!')\n",
    "else:\n",
    "    print(item_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>상품명</th>\n",
       "      <th>가격</th>\n",
       "      <th>판매 상태</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>홍피망 5kg</td>\n",
       "      <td>55,000원</td>\n",
       "      <td>판매중</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>화이트 아스파라거스(455g)</td>\n",
       "      <td>13,000원</td>\n",
       "      <td>품절</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>오크라 500g-상태b급</td>\n",
       "      <td>4,500원</td>\n",
       "      <td>품절</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>보리순(500g)</td>\n",
       "      <td>8,000원</td>\n",
       "      <td>품절</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>열매마 500g</td>\n",
       "      <td>6,000원</td>\n",
       "      <td>품절</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                상품명        가격 판매 상태\n",
       "0           홍피망 5kg  55,000원    판매중\n",
       "1  화이트 아스파라거스(455g)  13,000원     품절\n",
       "2     오크라 500g-상태b급   4,500원     품절\n",
       "3         보리순(500g)   8,000원     품절\n",
       "4          열매마 500g   6,000원     품절"
      ]
     },
     "execution_count": 49,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>상품명</th>\n",
       "      <th>가격</th>\n",
       "      <th>판매 상태</th>\n",
       "      <th>무게</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>홍피망 5kg</td>\n",
       "      <td>55,000원</td>\n",
       "      <td>판매중</td>\n",
       "      <td>5kg</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>화이트 아스파라거스(455g)</td>\n",
       "      <td>13,000원</td>\n",
       "      <td>품절</td>\n",
       "      <td>455g</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>오크라 500g-상태b급</td>\n",
       "      <td>4,500원</td>\n",
       "      <td>품절</td>\n",
       "      <td>500g</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>보리순(500g)</td>\n",
       "      <td>8,000원</td>\n",
       "      <td>품절</td>\n",
       "      <td>500g</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>열매마 500g</td>\n",
       "      <td>6,000원</td>\n",
       "      <td>품절</td>\n",
       "      <td>500g</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                상품명        가격 판매 상태    무게\n",
       "0           홍피망 5kg  55,000원    판매중   5kg\n",
       "1  화이트 아스파라거스(455g)  13,000원     품절  455g\n",
       "2     오크라 500g-상태b급   4,500원     품절  500g\n",
       "3         보리순(500g)   8,000원     품절  500g\n",
       "4          열매마 500g   6,000원     품절  500g"
      ]
     },
     "execution_count": 50,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "gram_tmp = df.상품명.str.extract('(\\d+g|\\d+kg)')\n",
    "df['무게'] = gram_tmp.dropna()\n",
    "df1 = df.dropna()\n",
    "df1.reset_index(inplace=True)\n",
    "del df1['index']\n",
    "df1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[5000, 455, 500, 500, 500]\n"
     ]
    }
   ],
   "source": [
    "# 무게만 추출\n",
    "gram_list = []\n",
    "for i in range(len(df1)):\n",
    "    tmp = df1.loc[i][3]\n",
    "    if 'kg' in tmp:\n",
    "        wei = tmp.split('kg')\n",
    "        res = int(wei[0])*1000\n",
    "    elif 'g' in tmp:\n",
    "        wei = tmp.split('g')\n",
    "        res = int(wei[0])\n",
    "    gram_list.append(res)\n",
    "print(gram_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[55000, 13000, 4500, 8000, 6000]"
      ]
     },
     "execution_count": 55,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 가격 추출\n",
    "plist = []\n",
    "for i in range(len(df1)):\n",
    "    tmp = df1.loc[i][1]\n",
    "    tmp1 = tmp.split('원')\n",
    "    tmp2 = tmp1[0].split(',')\n",
    "    tmp3 = ''.join(tmp2)\n",
    "    plist.append(int(tmp3))\n",
    "plist"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>상품명</th>\n",
       "      <th>가격</th>\n",
       "      <th>판매 상태</th>\n",
       "      <th>무게</th>\n",
       "      <th>가격/g</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>홍피망 5kg</td>\n",
       "      <td>55,000원</td>\n",
       "      <td>판매중</td>\n",
       "      <td>5kg</td>\n",
       "      <td>11원/g</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>화이트 아스파라거스(455g)</td>\n",
       "      <td>13,000원</td>\n",
       "      <td>품절</td>\n",
       "      <td>455g</td>\n",
       "      <td>28원/g</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>오크라 500g-상태b급</td>\n",
       "      <td>4,500원</td>\n",
       "      <td>품절</td>\n",
       "      <td>500g</td>\n",
       "      <td>9원/g</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>보리순(500g)</td>\n",
       "      <td>8,000원</td>\n",
       "      <td>품절</td>\n",
       "      <td>500g</td>\n",
       "      <td>16원/g</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>열매마 500g</td>\n",
       "      <td>6,000원</td>\n",
       "      <td>품절</td>\n",
       "      <td>500g</td>\n",
       "      <td>12원/g</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                상품명        가격 판매 상태    무게   가격/g\n",
       "0           홍피망 5kg  55,000원    판매중   5kg  11원/g\n",
       "1  화이트 아스파라거스(455g)  13,000원     품절  455g  28원/g\n",
       "2     오크라 500g-상태b급   4,500원     품절  500g   9원/g\n",
       "3         보리순(500g)   8,000원     품절  500g  16원/g\n",
       "4          열매마 500g   6,000원     품절  500g  12원/g"
      ]
     },
     "execution_count": 56,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 그램당 가격 추출하기\n",
    "GramPerPrice = []\n",
    "for i in range(len(df1)):\n",
    "    res = plist[i] // gram_list[i]\n",
    "    GramPerPrice.append(str(res)+'원/g')\n",
    "df1['가격/g'] = GramPerPrice\n",
    "df1"
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
