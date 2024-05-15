
    // Dữ liệu JSON về các xe ô tô
  var data =  {{ json_data|safe }};
  console.log(data);


// Số lượng xe trên mỗi trang
var itemsPerPage = 10;

// Tính số trang dựa trên số lượng xe và số lượng xe trên mỗi trang
var totalPages = Math.ceil(data.length / itemsPerPage);

// Lấy đối tượng tbody từ bảng
var tableBody = document.getElementById("car-table-body");

// Hiển thị dữ liệu của trang đầu tiên khi trang được tải
showPage(1);

// Hàm hiển thị dữ liệu cho một trang cụ thể
function showPage(pageNumber) {
    // Xóa nội dung của bảng trước khi hiển thị trang mới
    tableBody.innerHTML = "";

    // Tính chỉ số bắt đầu và chỉ số kết thúc của dữ liệu trên trang hiện tại
    var startIndex = (pageNumber - 1) * itemsPerPage;
    var endIndex = startIndex + itemsPerPage;

    // Lặp qua mỗi xe trên trang hiện tại và thêm nó vào bảng
    for (var i = startIndex; i < endIndex && i < data.length; i++) {
        var car = data[i];
        var row = tableBody.insertRow(0);
        var cell0 = row.insertCell(0);
        var cell1 = row.insertCell(1);
        var cell2 = row.insertCell(2);
        var cell3 = row.insertCell(3);
        var cell4 = row.insertCell(4);
        var cell5 = row.insertCell(5);
        var cell6 = row.insertCell(6);
        cell0.innerHTML = car.ID;
        cell1.innerHTML = car.BienSo;
        cell2.innerHTML = car.HangXe;
        cell3.innerHTML = car.LoaiXe;
        cell4.innerHTML = car.NamSX;
        cell5.innerHTML = car.Color;
        cell6.innerHTML = car.NgayNhap;
    }

    // Hiển thị phân trang
    showPagination(pageNumber);
}

// Hàm hiển thị các nút phân trang
function showPagination(currentPage) {
    var paginationContainer = document.querySelector(".pagination");
    paginationContainer.innerHTML = "";

    for (var i = 1; i <= totalPages; i++) {
        var paginationLink = document.createElement("a");
        paginationLink.textContent = i;
        paginationLink.href = "#";
        if (i === currentPage) {
            paginationLink.classList.add("active");
        }
        paginationLink.addEventListener("click", function (event) {
            event.preventDefault();
            showPage(parseInt(event.target.textContent));
        });
        paginationContainer.appendChild(paginationLink);
    }
}


document.getElementById('customer-table').addEventListener('click', function(event) {
  const targetRow = event.target.closest('tr');
  if (!targetRow) return;
  const column1Data = targetRow.querySelector('td:nth-child(1)').textContent;
  document.getElementById('dataID').cquerySelector('input').value = column1Data;

});