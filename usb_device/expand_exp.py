'''
Created on 2013/10/30

@author: DALALA
'''

exp_curve_Slime = [(0,0),
                   (1800,0),
                   (2250,105),
                   (2700,417),
                   (3150,938),
                   (3600,1666),
                   (4050,2604),
                   (4500,3749)
                   ]
exp_curve_Warrior = [(0,0),
                     (630,0),
                     (1845,261),
                     (3060,1042),
                     (4275,2343),
                     (5490,4165),
                     (6705,6508)
                     ]
exp_curve_Gnome = [(0,0),
                   (525,0),
                   (1830,209),
                   (3135,833),
                   (4440,1875),
                   (5745,3332),
                   (7050,5207),
                   (8355,7497),
                   ]
exp_curve_Wizard = [(0,0),
                    (1200,0),
                    (2850,105),
                    (4500,417),
                    (6150,938),
                    (7800,1666),
                    (9450,2604),
                    (11110,3749),
                    (12750,5103),
                    (14400,6664),
                    (16050,8434),
                    (17700,10413),
                    (19350,12599),
                    (21000,14994),
                    (22650,17597),
                    (24300,20409),
                    (25950,23428),
                    (27600,26656)
                    ]
exp_curve_Wolf = [(0,0),
                  (900,0),
                  (2250,157),
                  (3600,625),
                  (4950,1406),
                  (6300,2499),
                  (7650,3905),
                  (9000,5623),
                  (10350,7654),
                  (11700,9996),
                  (13050,12651)
                  ]
exp_curve_Hag = [(0,0),
                 (900,0),
                 (3600,157),
                 (6300,625),
                 (9000,1406),
                 (11700,2499),
                 (14400,3905),
                 (17100,5623),
                 (19800,7654),
                 (22500,9996),
                 (25200,12651),
                 (27900,15619),
                 (30600,18899),
                 (33300,22491),
                 (36000,26396),
                 (38700,30613),
                 (41400,35142),
                 (44100,39984),
                 (46800,45138)               
                 ]
exp_curve_Master = [(0,0),
                    (450,0),
                    (2400,105),
                    (4350,417),
                    (6300,938),
                    (8250,1666),
                    (10200,2604),
                    (12150,3749),
                    (14100,5103),
                    (16050,6664),
                    (18000,8434),
                    (19950,10413),
                    (21900,12599),
                    (23850,14994),
                    (25800,17597),
                    (27750,20409),
                    (29700,23428),
                    (31650,26656)
                    ]
def ShowExpCurve(exp_curve):
    for i,v in enumerate (exp_curve):
        if 0==i :
            continue
        print ("lv=%2d,serve=%5d,accum=%5d" % (i,v[0],v[1]))
def Find_lv(curve,exp):
    for curve_lv,(curve_serve,curve_accum) in enumerate(curve):
        if exp < curve_accum :
            break
    return (curve_lv-1,exp-curve[curve_lv-1][1])
def Feed_Card_1(src,feed):
    for src_lv,(src_serve,src_accum) in enumerate (src):
        if 0==src_lv:
            continue
        #print("lv=%2d,serve=%5d,accum=%5d" % (src_lv,src_serve,src_accum))
        for feed_lv,(feed_serve,feed_accum) in enumerate (feed):
            if 0==feed_lv:
                continue
            new_accum = src_accum + feed_serve
            (new_lv,overflow) = Find_lv(src,new_accum)
            print ("src_lv=%2d,src_accum=%5d,feed_lv=%2d,feed_serve=%5d => new_accum=%5d =>src_lv=%2d+overflow=%5d" % (src_lv,src_accum,feed_lv,feed_serve,new_accum,new_lv,overflow))
            
        
#ShowExpCurve(exp_curve_Master)
Feed_Card_1(exp_curve_Hag,exp_curve_Master)