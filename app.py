import ipfsApi
import streamlit as st

st.title('Decentralized Document Storage')

fileS=st.file_uploader('Upload Files',type=['txt'])

if fileS is not None:
    fileS_details={}
    fileS_details['type']=fileS.type
    fileS_details['size']=fileS.size
    st.write(fileS_details)
    with open('file.txt','wb') as f:
        f.write(fileS.getbuffer())
    
    api=ipfsApi.Client('127.0.0.1',5001)
    res=api.add('file.txt')
    st.success('http://127.0.0.1:8080/ipfs/'+res['Hash'])
    