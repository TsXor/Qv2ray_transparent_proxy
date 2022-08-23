import os, sys, subprocess, json, psutil

def get_qv_info():
  try:
    qv_proc = [proc for proc in psutil.process_iter() if proc.name() == 'qv2ray.exe'][0]
  except:
    raise RuntimeError('Qv2ray is not running!')
  qv_path = '\\'.join(qv_proc.cmdline()[0].split('\\')[:-1])
  os.chdir(qv_path)
  qv_conf_path = os.path.abspath('./config/Qv2ray.conf')
  with open(qv_conf_path) as qv_conf_file:
    qv_conf = qv_conf_file.read()
  qv_conf = json.loads(qv_conf)
  qv_socksport = qv_conf["inboundConfig"]["socksSettings"]["port"]
  #正常情况下是这样的
  qv_sysproxy = False if "systemProxySettings" in qv_conf["inboundConfig"] else True
  qv_kpath = qv_conf["kernelConfig"]["v2CorePath_win"]
  qv_kpath = os.path.abspath(qv_kpath)
  qv_kname = qv_kpath.split('\\')[-1]
  try:
    qv_kproc = [proc for proc in psutil.process_iter() if proc.name() == qv_kname][0]
  except:
    raise RuntimeError('Maybe you are not connected to any server!')
  return qv_socksport, qv_sysproxy, qv_kproc

def tp_run(port):
  path_t2s = '\\'.join(sys.argv[0].split('\\')[:-1])+'\\tun2socks'
  return subprocess.Popen('%s -device wintun -proxy socks5://127.0.0.1:%d'%(path_t2s,int(port)), stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def main():
  socksport, sysproxy, kproc = get_qv_info()
  if sysproxy:
    sys.exit(0)
  tp_subp = tp_run(socksport)
  psutil.wait_procs([kproc])
  tp_subp.kill()
  sys.exit(0)

if __name__ == '__main__':
  main()
