/*
 * API Abstraction
 */
function api(apiConnectType, url, data, asyncMode, callback, feedBack = false) {
    if (data)
        $.ajax({
            type: apiConnectType,
            url: url,
            async: asyncMode,
            data: JSON.stringify(data),
            dataType: "json",
            contentType: 'application/json',
            headers: {'X-CSRFToken': getCookie('csrftoken')},
            success: function (remoteData) {
                if (remoteData.status === true) {
                    if (callback !== null && typeof callback === "function") {
                        if (feedBack) {
                            swalSuccess(remoteData.message);
                            setTimeout(function () {
                                callback(remoteData.data);
                            }, 2000);
                        } else
                            callback(remoteData.data);
                    }
                } else {
                    swalWarning(remoteData.message);
                }
            },
            error: function (err) {
                if (feedBack)
                    swalError("An Unexpected error has occurred. Please try again or Contact Support!");
            }
        });

    if (data === null)
        $.ajax({
            type: apiConnectType,
            url: url,
            async: asyncMode,
            dataType: "json",
            contentType: 'application/json',
            headers: {'X-CSRFToken': getCookie('csrftoken')},
            success: function (remoteData) {
                if (remoteData.status === true) {
                    if (callback !== null && typeof callback === "function") {
                        if (feedBack) {
                            swalSuccess(remoteData.message);
                            setTimeout(function () {
                                callback(remoteData.data);
                            }, 2000);
                        } else
                            callback(remoteData.data);
                    }
                } else {
                    swalWarning(remoteData.message);
                }
            },
            error: function (err) {
                if (feedBack)
                    swalError("An Unexpected error has occurred. Please try again or Contact Support!");
            }
        });
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

/*
 * Date Methods
 */
function formatDate(date) {
    return moment(date).format("DD-MM-YYYY");
};
function formatDateShort(date) {
    return moment(date).format("MMM DD");
};
function formatDateCustom(date, format) {
    return moment(date).format(format);
};

/*
 * SWAL
 */
function swalWarning(message) {
    swalEngineNoCallBack("Wait a Minute...", message, "warning");
};
function swalWarningConfirm(message, callBack) {
    if (message === null)
        message = "This is a Sensitive Operation. Are you sure you want to Proceed";

    swalEngineCallBack("Wait a Minute...", message, "warning", "btn-success", "btn-warning", callBack);
};
function swalInfo(message) {
    swalEngineNoCallBack("Information", message, "info", false);
};
function swalError(message) {
    swalEngineNoCallBack("Oops. There seems to be a Problem", message, "error");
};
function swalEx() {
    swalError("This is embarassing but something serious actually is wrong. Please check with Support");
};
function swalSuccess(message) {
    swalEngineNoCallBack("Awesome", message, "success", false);
};

function swalEngineNoCallBack(title, message, type, showConfirmButton = true) {
    if (showConfirmButton)
        Swal.fire({
            title: title,
            text: message,
            icon: type,
            showCancelButton: false,
            showConfirmButton : showConfirmButton,
            confirmButtonColor: "#556ee6"
        });
    else
        Swal.fire({
            title: title,
            text: message,
            icon: type,
            showCancelButton: false,
            showConfirmButton: showConfirmButton,
            confirmButtonColor: "#556ee6",
            timer: 3000
        });
};

function swalEngineCallBack(title, message, type, confirmButtonClass, cancelButtonClass, callback) {
    Swal.fire({
        title: title,
        text: message,
        icon: type,
        showCancelButton: true,
        showConfirmButton: true,
        confirmButtonText: "Okay"
    }).then((result) => {
        if (result.isConfirmed)
            callback();
    });
};

// ReSharper disable once NativeTypePrototypeExtending
Number.prototype.format = function (n, x) {
    var re = '\\d(?=(\\d{' + (x || 3) + '})+' + (n > 0 ? '\\.' : '$') + ')';
    return this.toFixed(Math.max(0, ~~n)).replace(new RegExp(re, 'g'), '$&,');
};