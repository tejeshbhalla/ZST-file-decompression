import datetime
import io
import zstandard as zstd
import json
import pandas as pd

#print('Start Time: ', datetime.datetime.now())
path = "C:\\Users\\VrushabhKaushik\\Downloads\\RC_2019-02.zst"
i = 0
with open(path, 'rb') as fh:
    dctx = zstd.ZstdDecompressor()
    stream_reader = dctx.stream_reader(fh)
    text_stream = io.TextIOWrapper(stream_reader, encoding='utf-8')
    z = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
    x = []
    for lines in text_stream:
        lines=json.loads(lines.translate(z))
        x.append(lines)
        i+=1

df = pd.DataFrame(x)
'''rename columns as per your needs'''
#df.rename(columns={0:'parent_id', 1:'body', 2:'score', 3: 'created_utc', 4:'subreddit_id'}, inplace=True)
export_excel = df.to_excel (r'C:\\Users\\VrushabhKaushik\\Downloads\\export_dataframe.xlsx', index = None, header=True)
#print(df)
#print('End Time: ', datetime.datetime.now())
#print('Total lines read: ', i)
