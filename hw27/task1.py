# ���� ������, ������ ������� �������� � ��� ������� � ���������� ������������ ���������� ����:
#
# { "name": "Allen Raymond", "email": "nulla.ante@vestibul.co.uk", "phone": "(992) 914-3792",
# "favorite": False, }
# ������� �������� ��� ������������ name, ��� email, ���������� ����� phone � �������� favorite
# � ��������� ������� ��� ���.
#
# ������������ ��� ������� ��� ������������ � �������������� ������ ��������� � ������� ������
# json � �������� ���������� ������ � ��������� �����.
#
# ������ ������� write_contacts_to_file ��������� ��� ���������: filename � ��� �����,
# contacts � ������ ���������. ��� ��������� ��������� ������ � ����, ��������� ����� dump
# ������ json.
#
# ��������� json ����� ������ ���� ���������:
#
# { "contacts": [ { "name": "Allen Raymond", "email": "nulla.ante@vestibul.co.uk",
# "phone": "(992) 914-3792", "favorite": false }, ... ] }
# �.�. ������ ��������� ������ ��������� �� ����� "contacts", � �� ������ ��������� ��� � ����.
#
# ������ ������� read_contacts_from_file ������ � ���������� ��������� ������ contacts ��
# ����� filename, ������������ ����� �������� write_contacts_to_file, ��������� ����� load
# ������ json.
import json


def write_contacts_to_file(filename, contacts):


def read_contacts_from_file(filename):
