$(document).ready(function() {
            loadListRequest();
            loadListOptionsRequest();
        });

function loadListOptionsRequest(){
    api('GET', '/api/shoppinglist/getshoppingliststatusoptions/', null, true, loadListOptionsResponse);
}

function loadListOptionsResponse(data)
{
    let selStatus = document.getElementById('selStatus');
    selStatus.options[0] = new Option('Select Status', '---');

     $.each(data,
        function(i, datum) {
            selStatus.options[datum.keyValue + 1] = new Option(datum.keyName, datum.keyValue);
        });
}

function loadListRequest(){
    api('GET', '/api/shoppinglist/getshoppinglist/', null, true, loadListResponse);
}

function loadListResponse(data)
{
    $("#list-table tbody").empty();

    $("#txtItemId").val(0);

    $.each(data,
        function(i, datum) {
            let rowData = '<tr>';
            rowData += '<td>';
            rowData += '<h5 class="text-truncate font-size-14 mb-1">';
            rowData += '<a href="javascript: void(0);" class="text-dark">' + datum.itemName + '</a>';
            rowData += '</h5>';
            rowData += '<p class="btn btn-sm w-lg mb-0 ' + getVisualClass(datum.itemStatus) + '">' + datum.itemStatusText + '</p>';
            rowData += '</td>';

            rowData += '<td style="width: 90px;">';
            rowData += '<div>';

            rowData += '<ul class="list-inline mb-0 font-size-16">';
            rowData += '<li class="list-inline-item">';
            rowData += '<a data-bs-toggle="modal" data-bs-target="#staticBackdrop" onclick="getListItemRequest(' + datum.id + ')" class="text-success p-1">';
            rowData += '<i class="bx bxs-edit-alt"></i></a></li>';

            rowData += '<li class="list-inline-item">';
            rowData += '<a onclick="removeItemRequest(' + datum.id + ');" class="text-danger p-1"><i class="bx bxs-trash"></i></a>';
            rowData += '</li>';
            rowData += '</ul>';

            rowData += '</div>';
            rowData += '</td>';

            rowData += '</tr>';

            $("#list-table tbody").append(rowData);
        });

    $("#itemCount").text(data.length);
}

function getVisualClass(statusId)
{
    switch(statusId){
        case 0: return "btn-secondary";
        case 1: return "btn-info";
        case 2: return "btn-danger";
        case 3: return "btn-warning";
        case 4: return "btn-dark";
        case 5: return "btn-success";
        default: return "btn-primary";
    }
}

function addList()
{
    if ($("#txtItemName").val() === "")
    {
        swalWarning('Enter an Item Name');
        return;
    }

    if ($("#selStatus").val() === "---")
    {
        swalWarning('Select a Valid Status');
        return;
    }

    if ($("#txtMarketAmount").val() === "")
        $("#txtMarketAmount").val(0);

    addListRequest({
        "id": $("#txtItemId").val(),
        "itemName": $("#txtItemName").val(),
        "itemStatus": $("#selStatus").val(),
        "marketAmount": $("#txtMarketAmount").val()
    }, true);
}

function addListQuick()
{
    if ($("#txtQuickAdd").val() === "")
    {
        swalWarning('Enter an Item Name to use Quick Add');
        return;
    }

    addListRequest({
        "itemName": $("#txtQuickAdd").val()
    }, false);
}

function addListRequest(requestData, feedback)
{
    window.api('POST', '/api/shoppinglist/postshoppinglist/', requestData, true, addListResponse, feedback);
}

function addListResponse(data)
{
    $("#txtQuickAdd").val('');
    $("#txtItemId").val('');
    $("#txtItemName").val('');
    $("#selStatus").val('---');
    $("#txtMarketAmount").val(0);

    loadListRequest();
}

function removeItemRequest(itemId)
{
    swalWarningConfirm('Are you sure you want to remove this Item?', function(){
        api('POST', '/api/shoppinglist/deleteshoppinglist/', {
            "id": itemId
        }, true, removeItemResponse);
    });
}

function removeItemResponse(data)
{
    loadListRequest();
}

function getListItemRequest(itemId)
{
    api('GET', '/api/shoppinglist/getshoppinglistitem/' + itemId, null, true, getListItemResponse);
}

function getListItemResponse(data)
{
    $("#txtItemId").val(data.id);
    $("#txtItemName").val(data.itemName);
    $("#selStatus").val(data.itemStatus);
    $("#txtMarketAmount").val(data.marketAmount);
}

function clearShoppingList()
{
    swalWarningConfirm(
        'Are you sure you want clear this ENTIRE list? This operations is irreversible. All saved data will be lost!',
        function(){api('POST', '/api/shoppinglist/clearshoppinglist/', null, true,
        clearShoppingListResponse);
    });
}

function clearShoppingListResponse(data) {
    loadListRequest();
    swalInfo('Shopping List Cleared');
}