snes2hex = lambda address: address >> 1 & 0x3F8000 | address & 0x7FFF

snesAdrs = [0x00088000, 0x000886DE, 0x00088E14, 0x0008953A, 0x00089C2A, 0x0008A322, 0x0008AA7E, 0x0008B1BE, 0x0008B8AC, 0x0008BFE4, 0x0008C6B8, 0x0008CF52, 0x0008D89C, 0x0008E240, 0x0008EC2E, 0x0009F5EC, 0x00098000, 0x00098ABC, 0x00099390, 0x00099C6C, 0x0009A68C, 0x0009B038, 0x0009B9E0, 0x0009C388, 0x0009CD44, 0x0009D704, 0x0009E0D0, 0x0009EAA6, 0x000AF3B6, 0x000A8000, 0x000A8AB2, 0x000A93DA, 0x000A9D38, 0x000AA5F0, 0x000AAF30, 0x000AB8AA, 0x000AC252, 0x000ACBF2, 0x000AD4A0, 0x000ADDE2, 0x000AE712, 0x000BF0D2, 0x000B8000, 0x000B88EC, 0x000B916A, 0x000B99BA, 0x000BA380, 0x000BAD58, 0x000BB5BC, 0x000BBE74, 0x000BC708, 0x000BD1CC, 0x000BDAA4, 0x000BE4E8, 0x000BED5C, 0x000CF58E, 0x000C8000, 0x000C8932, 0x000C94BC, 0x000C9E7A, 0x000CA7BC, 0x000CB21E, 0x000CBCBC, 0x000CC6F6, 0x000CD1B0, 0x000CDC16, 0x000CE7F8, 0x000DF39A, 0x000D8000, 0x000D8904, 0x000D96E0, 0x000D9FF0, 0x000DA998, 0x000DB1D6, 0x000DBC04, 0x000DC5C6, 0x000DD12C, 0x000DD9FE, 0x000DE298, 0x000DEBD2, 0x000EF642, 0x000E8000, 0x000E89BA, 0x000E93F0, 0x000EA090, 0x000EA8DE, 0x000EB1A6, 0x000EBB4A, 0x000EC40E, 0x000ECCAC, 0x000ED65C, 0x000EE0DE, 0x000EEB5C, 0x000FF572, 0x000F8000, 0x000F8A54, 0x000F93A4, 0x000F9F4A, 0x000FA9E0, 0x000FB1EC, 0x000FBC50, 0x000FC570, 0x000FCFE8, 0x000FD906, 0x000FE332, 0x0010EDEE, 0x00108000, 0x00108998, 0x00109242, 0x00109D8E, 0x0010AB96, 0x0010AE76, 0x0010B19C, 0x0010B326, 0x0010B534, 0x0010B894, 0x0010BBA4, 0x0010C8B8, 0x0010D528, 0x0010DEBA, 0x0011EB38, 0x00118000, 0x00118C6A, 0x00119616, 0x0011A370, 0x0011AB90, 0x0011B5B6, 0x0011C092, 0x0011C458, 0x0011CA62, 0x0011CDB6, 0x0011D1B2, 0x0011D5D6, 0x0011D934, 0x0011DF92, 0x0011E0B2, 0x0011E3E0, 0x0011E75C, 0x0011E89C, 0x0012EBF6, 0x00128000, 0x0012A1C2, 0x0012AFD2, 0x0012C10C, 0x0012C816, 0x0012D1A0, 0x0013DC5A, 0x00138000, 0x00139516, 0x0013A4D4, 0x0013B58E, 0x0013C662, 0x0014DB7A, 0x00148000, 0x00148EBC, 0x00149D1C, 0x0014AFC0, 0x0014BF3E, 0x0014C7E6, 0x0014D85A, 0x0015EC58, 0x00158000, 0x0015959A, 0x00159FDE, 0x0015ACD4, 0x0015BCF0, 0x0015CA82, 0x0015D250, 0x0016F38E, 0x00168000, 0x00168A38, 0x0016947E, 0x00169F4A, 0x0016BBAE, 0x0017CBF2, 0x00178000, 0x0017A45C, 0x0017C646, 0x0017E0EE, 0x0017ECC4, 0x0017EE0E, 0x0017F00E, 0x0017F20E, 0x0017F40E, 0x0017F60E, 0x0017F80E, 0x0017FA0E, 0x0018FC0E, 0x00188000, 0x00188200, 0x00188400, 0x00188600, 0x00188800, 0x00188A00, 0x00188C00, 0x00188E00, 0x00189000, 0x00189200, 0x00189400, 0x00189600, 0x00189800, 0x00189A00, 0x00189C00, 0x00189E00, 0x0018A000, 0x0018A200, 0x0018A400, 0x0018A600]

import struct
rompath = "Mario & Wario.sfc"
outpath = "OUT/"

def getB(number=1):
    return int.from_bytes(rom.read(number), byteorder='little')

def getQue(num):
    que = []
    u = format(num, '016b')
    for i in range(0,16,2):
        que.append(int("0b"+u[i:i+2], 2))
    return que

def getROL(num):
    d = num & 0x000F
    c = (num & 0x00F0) >> 4
    b = (num & 0x0F00) >> 8
    a = (num & 0xF000) >> 12
    return [a,b,c,d]

lzadr  = 0xB7CE
lzsize = 0x20

HDRSIZE = 8
WARNLIMIT = 2
EXEMPTLIST = [(0xFF, 0x7F, 0x323A), (0x5F, 0x02, 0x02DF), (0xDF, 0x57, 0x2FBF), (0xBF, 0x2B, 0x073F)]


with open(rompath, "rb") as rom:
    rom.seek(lzadr)
    lz  = list(struct.unpack("<{:d}h".format(lzsize >> 1), rom.read(lzsize)))
    
    
    for infile in range(0,len(snesAdrs)):
        snesadr = snesAdrs[infile]
        warning = 0
        exempt_flag = False
        
        while True:
            if warning == WARNLIMIT:
                break
            
            root = snes2hex(snesadr)
            
            startAdr = root
            rom.seek(root)
            ha, hb, hc, datSeed, rolRel, eof = struct.unpack("<BBBBHH", rom.read(HDRSIZE))
            #print("header - {:02X} {:02X} {:02X} {:02X} {:04X} {:04X}".format(ha, hb, hc, datSeed, rolRel, eof))
            
            if (hc, datSeed, rolRel) in EXEMPTLIST:
                rom.seek(rom.tell()-8)
                exempt_data = rom.read(0x200)
                exempt_flag = True
                break
            
            if ha != 8:
                #print("FP {:06X}\t{:06X}. Fixing...".format(snesadr,startAdr))
                snesadr -= 0x010000
                warning += 1
                continue
            break
        
        if warning == WARNLIMIT:
            #print("not worth it.")
            continue
        
        DATSIZE = datSeed << 8
        
        datadr = root + HDRSIZE
        libadr = root + DATSIZE + HDRSIZE
        roladr = root + rolRel
        
        libStep = 0
        rolStep = 0
        
        activeROL = []
        
        if exempt_flag:
            otype = "_r"
        else:
            otype = "_c"
        with open(outpath+"{:03d}_{:08X}{:s}.smc".format(infile, root, otype), "wb+") as out:
            
            rom.seek(datadr)
            dat = list(struct.unpack("<{:d}H".format(DATSIZE >> 1), rom.read(DATSIZE)))
            
            while True:
                if exempt_flag:
                    out.write(exempt_data)
                    exempt_flag = False
                    print("EX {:03d}\t{:06X} - {:06X}".format(infile, startAdr, startAdr+0x1FF))
                    break
                
                
                datQue = getQue(dat.pop(0))
                for ins in datQue:
                    if ins == 0:
                        rta = rom.tell()
                        rom.seek(libadr + libStep)
                        newLib = getB(2)
                        libStep += 2
                        rom.seek(rta)
                        out.write(newLib.to_bytes(2, byteorder='little'))
                        continue
                    
                    elif ins == 1:
                        print("FUCKFUCKFUCK")
                        continue
                    
                    elif ins == 2:
                        if not activeROL:
                            rta = rom.tell()
                            rom.seek(roladr + rolStep)
                            newRol = getB(2)
                            endAdr = rom.tell()-1
                            rolStep += 2
                            rom.seek(rta)
                            activeROL = getROL(newRol)
                        jump = lz[activeROL.pop(0)]
                    
                    #case 3, mutta suoritetaan aina, oli 2 tai 3
                    rta = out.tell()
                    out.seek(rta+jump)
                    past = int.from_bytes(out.read(2), byteorder='little')
                    out.seek(rta)
                    out.write(past.to_bytes(2, byteorder='little'))
                
                if out.tell() == eof:
                    print("OK {:03d}\t{:06X} - {:06X}".format(infile, startAdr, endAdr))
                    break
