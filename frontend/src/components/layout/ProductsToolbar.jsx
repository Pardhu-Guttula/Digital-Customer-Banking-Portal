import React, { useId } from "react";
import ResultsText from "../ui/ResultsText";
import SortControl from "../ui/SortControl";
import ViewToggle from "../ui/ViewToggle";

export default function ProductsToolbar({
  shownCount = 12,
  totalCount = 20,
  sortValue = "",
  sortOptions = [],
  onSortChange = () => {},
  view = "grid",
  onViewChange = () => {},
}) {
  const sortId = useId();

  return (
    <header className="w-full">
      <div
        className={[
          "w-full rounded-[12px] bg-white px-[20px] py-[16px]",
          "shadow-[0px_1px_3px_0px_rgba(0,0,0,0.1),0px_1px_2px_0px_rgba(0,0,0,0.06)]",
          "flex flex-col gap-3",
          "sm:flex-row sm:items-center sm:justify-between sm:gap-6",
        ].join(" ")}
      >
        <ResultsText shownCount={shownCount} totalCount={totalCount} />

        <div className="flex items-center justify-between gap-[20px] sm:justify-end">
          <SortControl
            id={sortId}
            value={sortValue}
            options={sortOptions}
            onChange={onSortChange}
          />
          <ViewToggle value={view} onChange={onViewChange} />
        </div>
      </div>
    </header>
  );
}