USE fastapi;

-- Username,  Password, Identity
INSERT INTO Information VALUES ('admin1', '123', 'Manager');
INSERT INTO Information VALUES ('admin2', '123', 'Manager');
INSERT INTO Information VALUES ('admin3', '123', 'Manager');
INSERT INTO Information VALUES ('admin4', '123', 'Manager');
INSERT INTO Information VALUES ('admin5', '123', 'Manager');
-- INSERT INTO Information VALUES ('', '', '');
-- INSERT INTO Information VALUES ('', '', '');
-- INSERT INTO Information VALUES ('', '', '');
-- INSERT INTO Information VALUES ('', '', '');
-- INSERT INTO Information VALUES ('', '', '');
-- INSERT INTO Information VALUES ('', '', '');
-- INSERT INTO Information VALUES ('', '', '');


-- Belong, Name, Manager_id
INSERT INTO Shop (Shop_id, Belong, Name, Manager_id) VALUES (1, '美食园', '煎饼', 'admin1');
INSERT INTO Shop (Shop_id, Belong, Name, Manager_id) VALUES (2, '美食园', '麻辣香锅', 'admin2');
INSERT INTO Shop (Shop_id, Belong, Name, Manager_id) VALUES (3, '美食园', '湘里香外', 'admin3');
INSERT INTO Shop (Shop_id, Belong, Name, Manager_id) VALUES (4, '美食园', '强子烤冷面', 'admin4');
INSERT INTO Shop (Shop_id, Belong, Name, Manager_id) VALUES (5, '美食园', '沙县小吃', 'admin5');
-- INSERT INTO Shop ('Shop_id', 'Belong', 'Name', 'Manager_id') VALUES ('', '', '', '');
-- INSERT INTO Shop ('Shop_id', 'Belong', 'Name', 'Manager_id') VALUES ('', '', '', '');
-- INSERT INTO Shop ('Shop_id', 'Belong', 'Name', 'Manager_id') VALUES ('', '', '', '');
-- INSERT INTO Shop ('Shop_id', 'Belong', 'Name', 'Manager_id') VALUES ('', '', '', '');
-- INSERT INTO Shop ('Shop_id', 'Belong', 'Name', 'Manager_id') VALUES ('', '', '', '');
-- INSERT INTO Shop ('Shop_id', 'Belong', 'Name', 'Manager_id') VALUES ('', '', '', '');
-- INSERT INTO Shop ('Shop_id', 'Belong', 'Name', 'Manager_id') VALUES ('', '', '', '');
-- INSERT INTO Shop ('Shop_id', 'Belong', 'Name', 'Manager_id') VALUES ('', '', '', '');
-- INSERT INTO Shop ('Shop_id', 'Belong', 'Name', 'Manager_id') VALUES ('', '', '', '');

SELECT 'End Insert' as 'Result:';
