
SELECT TOP (1000) [STT] Car_id
      ,[Ti?n C? Ph?n] Gia, N'C? ph?n' Note,1 Cost
      ,[C? ?ông],b.id [Holder_id]
	  into #temp
  FROM [CarSale].[dbo].['B?ng TH T1$'_xlnm#_FilterDatabase] a left join Category_holder b on a.[C? ?ông] =b.name where [C? ?ông] is not null 
  insert #temp
  SELECT TOP (1000) [STT]
      ,[Master car], N'C? ph?n' Note,1 Cost
      ,'Master car',1
  FROM [CarSale].[dbo].['B?ng TH T1$'_xlnm#_FilterDatabase] 
  select * from #temp order by Car_id,Holder_id
   SELECT TOP (1000) [id]
      ,[Gia]
      ,[Note]
      ,[Car_id]
      ,[Cost]
      ,[Holder_id]
  FROM [CarSale].[dbo].[Category_cardetail]

  insert [Category_cardetail]([Gia],[Note]      ,[Car_id]      ,[Cost]      ,[Holder_id])   select Gia,Note,Car_id,Cost,Holder_id from #temp order by Car_id,Holder_id
  drop  table #temp
  SELECT *FROM [CarSale].[dbo].[Category_cardetail]
select * from Category_car a left join [Category_cardetail] b on a.id=b.Car_id left join Category_holder c on b.Holder_id = c.id order by a.id
SELECT * from [Category_car] a left join  [Category_cardetail] b on a.id =b.Car_id and b.Holder_id =1 left join [Category_cardetail] c on a.id=c.Car_id and c.Holder_id!=1
 insert #temp select stt   ,N'Hoa H?ng bán xe' Note   ,[Hoa H?ng bán xe]  FROM [CarSale].[dbo].['B?ng TH T1$'_xlnm#_FilterDatabase] where       [Hoa H?ng bán xe] is not null
 select * from #temp
insert [Category_cardetail]([Gia],[Note]      ,[Car_id]      ,[Cost]      ,[Holder_id])   select [Hoa H?ng mua xe],Note,stt,2,1 from #temp order by stt