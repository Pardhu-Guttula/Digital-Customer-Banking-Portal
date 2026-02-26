import React from "react";

export default function IconToggleButton({
  active = false,
  ariaLabel,
  icon: Icon,
  onClick = () => {},
}) {
  return (
    <button
      type="button"
      onClick={onClick}
      aria-label={ariaLabel}
      aria-pressed={active}
      className={[
        "h-[40px] w-[40px] rounded-[8px] inline-flex items-center justify-center",
        "transition-colors",
        active ? "bg-[#4361ee] text-white" : "bg-[#F1F5F9] text-[#64748B]",
        "focus:outline-none focus-visible:ring-2 focus-visible:ring-[#4361ee]/35 focus-visible:ring-offset-2 focus-visible:ring-offset-white",
      ].join(" ")}
    >
      <Icon className="h-4 w-4" aria-hidden="true" />
    </button>
  );
}