USE `hockeydb`;
DROP procedure IF EXISTS `sortPlayersByAwards`;

DELIMITER $$
USE `hockeydb`$$
CREATE PROCEDURE `sortPlayersByAwards` ()
BEGIN
	select year, playerID, count(playerID) as total from `hockeydb`.`awardsplayers` group by playerID, year order by year, total desc;
END$$

DELIMITER ;

select coachID, year, w from `hockeydb`.`coaches` order by year, w desc

-- order the coaches by regular season wins for each year