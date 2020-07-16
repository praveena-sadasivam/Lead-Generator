import re
patterns1=[r'[0-9|a-zA-Z]*\s[a-z|A-Z|0-9]*\s[A-Z|a-z|0-9]*\s[A-Z|a-z|0-9]*[,]\s[A-Z]{2}[\s][0-9]{5}',
r'[0-9|A-Z|a-z ]*\n[A-Z|a-z ]*\n\t\t\t\t\t[A-Z|a-z]*[,]\s[A-Z]{2}\s[0-9]{5}',
r'[0-9|A-Z|a-z]*\s[A-Z|a-z|0-9]*\s[A-Z|a-z|0-9]*[, ]\s[A-Z|a-z]*\s[0-9]*\n[A-Z|a-z\s]*[,]\s[A-Z]{2}\s[0-9]{5}',
r'^\s[0-9]{3}\s[a-z|A-Z|0-9\s]*[,]\s[0-9|a-z|A-Z]*\s[a-z|A-Z]*\n[A-Z|a-z\s]*[, ]\s[A-Z]{2}\s[0-9]{5}',
r'^[0-9a-zA-Z ]*[, ]\s[0-9A-Za-z\s]*[, ]\s[a-zA-z\s]*[0-9a-zA-z]{5}\n\bUnited States|USA\b$',
r'^[0-9]{3}[a-z|A-Z\s]*\s[a-z|A-Z]{2}.[A-Z|a-z]*\s[0-9]*[A-z|a-z|0-9]*[,]\s[A-Z]{2}\s[0-9]{5}$',
r'^[a-z|A-Z|0-9]*[,]\s[A-z]{2}\s[0-9]{5}\r\n\bUnited States\b',
r'[0-9]*\s[A-z].\s[a-z|0-9]*\s[A-Z|a-z]*.\n[A-Za-z]*\s[A-z|a-z]*[, ]\s[A-Z]{2}\s[0-9]{5}\n\bUSA\b']



patterns2=[r'^[A-Z|a-z]\s[A-Z|a-z ]\n[0-9]\s[A-Z|a-z]\s[A-Z|a-z]\n[A-z|a-z]\s[A-Z|a-z]\s[A-Z]\s[0-9]{5}\s[A-z]*$',
r'[/|0-9|A-z]*[0-9|A-z|,]*\s[A-z|.|a-z|0-9]*[0-9|a-z|.]*[A-z|,|0-9]*\s[A-z|.|-]*[0-9|\s]*[A-z|,]*\s[A-z]*\s[0-9]{5}',
r'^[0-9|A-Z|a-z|,| ]*[-|0-9|.]*\n[A-Z|a-z]*[,]\s[A-Z|0-9]*\s[0-9A-Z]{3}[0-9|]*',
r'[0-9]*\s[0-9]*[a-z]*\s[A-z]*\s[#0-9]*\n[A-z]*\s[A-z]*[,]\s[A-z]{2}\s[0-9]{5}',
r'^[A-z|a-z|0-9]*\s[A-z|0-9|\s]*[A-z|\s|,|.]\s[0-9|A-Z|a-z]*\n[0-9|a-z]*\s[A-Z|a-z|0-9]*[,]\s[A-Z|a-z]*',
r'[0-9]*\s[a-z]*\s[A-Z|a-z]*\s[A-Z|a-z]*[,]\s[A-z]*\s[A-z]*\s[\w]*\s[\w]*\s[0-9][,]\s[0-9]{5}\s[A-z]*',
r'^[0-9]{3}\s[A-z|a-z|]\s[A-Z|a-z|,]\s[A-Z|a-z]\s[0-9|A-Z|a-z,]\s[A-Z]*\s[0-9]{5}',
r'^[A-Z|a-z|][0-9]\s[A-Z|a-z]{5}\s[A-Z|a-z]\s[A-Z|a-z]\s[A-Z|a-z,]\s[A-Z]\s[A-Z|0-9]\s[0-9|A-Z]\s[A-Z|a-z]*$',
r'[A-Z|a-z]\s[A-Z|a-z|0-9]\s[A-Z|a-z]\s[A-Z|a-z]\s#[0-9|A-z|a-z]\s[A-z|a-z,]\s[A-Z]{2}\s[0-9]{5}',
r'^[A-Z|a-z|]\s[A-Z|a-z],\s[A-Z]{3}\n[A-Z|a-z]\s[A-Z|a-z|0-9]\s[A-Z|a-z]\s[A-z|a-z,]\s[0-9][a-z]\s[A-Z|a-z,]\s[A-Z|a-z,]\s[A-Z|a-z]\s[A-Z|a-z,]\s[A-Z]\s|-|[0-9]{5}$',
r'[A-Z|a-z]\s[A-Z|a-z|0-9]\s[A-Z|a-z]\s[A-Z|a-z]\s#[0-9|A-z|a-z]\s[A-z|a-z,]\s[A-Z]{2}\s[0-9]{5}',
r'[A-z]*\s[0-9]{2}[,]\s[A-z]*\s[A-z]{3}[,]\s[A-z]*\s[A-z]{6}[0-9]{3}\s[A-z]*\s[A-z]*[A-z]*[,]\s[A-Z]{3}\s[0-9]{4}']