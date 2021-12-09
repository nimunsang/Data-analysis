#!/usr/bin/env python
# coding: utf-8

# In[334]:


import pandas as pd
import numpy as np
import requests


# In[335]:


# Riot Developer Portal에서 받은 API KEY입니다.
# 해당 값을 포함한 모든 종류의 KEY는 코드에 직접적으로 노출되지 않도록 하는 것이 좋습니다.
api_key = 'RGAPI-c65a463e-dfb7-47ec-bb93-09003053f757'

# 본인 소환사명입니다.
summoner_name = 'bbo bbo'


# In[336]:


# SUMMONER-V4 API URL
requesturl = 'https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/'+summoner_name+'?api_key='+api_key


# In[337]:


r = requests.get(requesturl)


# In[338]:


# 불러온 데이터 확인
r.json()


# In[339]:


# 본인 puuid입니다.
summoner_puuid = r.json()['puuid']


# In[340]:


# MATCH-V5 API URL
requesturl = 'https://asia.api.riotgames.com/lol/match/v5/matches/by-puuid/'+summoner_puuid+'/ids?start=0&count=20&api_key='+api_key


# In[341]:


r = requests.get(requesturl)


# In[342]:


# 불러온 데이터 확인
r.json()


# In[343]:


# 데이터 가져올 matchId입니다.
matchId = r.json()[0]


# In[344]:


# MATCH-V5 API URL
requesturl = 'https://asia.api.riotgames.com/lol/match/v5/matches/'+matchId+'?api_key='+api_key


# In[345]:


requesturl


# In[346]:


r = requests.get(requesturl)


# In[347]:


# 불러온 데이터 확인
r.json()


# In[348]:


# 모든 column print하게 설정 변경
pd.set_option('display.max_columns',None)


# In[349]:


# DataFrame으로 변환
df = pd.DataFrame(r.json()['info']['participants'])


# In[350]:


# 확인할 변수
COLUMNS = ['summonerName','teamId','win','visionScore']


# In[351]:


# 확인할 변수만 가져와서 새로운 DataFrame에 저장
df2 = df[COLUMNS]


# In[352]:


# 최종 추출 형태 확인
df2


# In[353]:


df = pd.DataFrame(r.json()['info']['teams'])


# In[354]:


COLUMNS = ['teamId', 'win']


# In[355]:


df3 = df[COLUMNS]


# In[356]:


df3


# In[357]:


df4 = df3.copy()


# In[358]:


team1_visionScore = 0
for i in range(0, 5):
    team1_visionScore += (r.json()['info']['participants'][i]['visionScore'])


# In[359]:


team2_visionScore = 0
for i in range(5, 10):
    team2_visionScore += (r.json()['info']['participants'][i]['visionScore'])


# In[360]:


df4['team_visionScore'] = [team1_visionScore, team2_visionScore]


# In[361]:


df4


# In[362]:


COLUMNS = ['win', 'team_visionScore']


# In[363]:


df5 = df4[COLUMNS]


# In[364]:


df5


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




