git chown -R root:root czaOrz  # ������Ŀ¼���������Ŀ¼��Ȩ��


�����Լ��ķ�������
1���ڷ������ˣ�
���� mkdir /gits/cza.git  ����·��
Ȼ�� git init --bare /gits/cza.git  ��ʼ��
��   chown -R cza:cza /gits/cza.git ��Ȩ

Ȼ��Ϳ���Զ������֧�ˣ����ǻ�Ҫ��Ҫ�ڷ������˵�/etc/.ssh����������
RSAAuthentication yes
PubkeyAuthentication yes
AuthorizedKeysFile .ssh/authorized_keys

���ض������룬��ע��ssh
ssh czaOrz@47.101.42.79 'cat >> .ssh/authorized_keys' < ~/.ssh/id_rsa.pub
git clone czaOrz@47.101.42.79:/gits/czaOrz.git


