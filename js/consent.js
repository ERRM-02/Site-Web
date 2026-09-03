/* Consentement et services tiers, chargé après l'analyse du document. */
tarteaucitron.init({
    privacyUrl: "mentions-legales",
    bodyPosition: "bottom",
    hashtag: "#tarteaucitron",
    cookieName: "tarteaucitron",
    orientation: "bottom",
    groupServices: false,
    showDetailsOnClick: true,
    serviceDefaultState: "wait",
    showAlertSmall: false,
    cookieslist: false,
    closePopup: false,
    showIcon: true,
    iconPosition: "BottomLeft",
    adblocker: false,
    DenyAllCta: true,
    AcceptAllCta: true,
    highPrivacy: true,
    handleBrowserDNTRequest: false,
    removeCredit: true,
    moreInfoLink: true,
    useExternalCss: false,
    useExternalJs: false,
    readmoreLink: "",
    mandatory: true,
    mandatoryCta: true
});

tarteaucitron.user.gtagUa = "G-G3J7LPT8J7";
tarteaucitron.user.gtagMore = function () {};
(tarteaucitron.job = tarteaucitron.job || []).push("gtag");

if (document.querySelector(".tac_iframe")) {
    (tarteaucitron.job = tarteaucitron.job || []).push("iframe");
}
