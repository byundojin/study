import tv
import remote

tv1 = tv.KoreanTV()
remote1 = remote.KoreanRetote(tv1)
remote1.volume_up()

remote2 = remote.ChineseRemote(tv1)
remote2.volume_up()

tv2 = tv.ChineseTV()
remote3 = remote.KoreanRetote(tv2)
remote3.volume_up()

remote3 = remote.ChineseRemote(tv2)
remote3.volume_up()