// Fill out your copyright notice in the Description page of Project Settings.


#include "UEAutoTrimSystem.h"

#include "CanvasItem.h"
#include "Debug/DebugDrawService.h"
#include "Engine/Canvas.h"

TAutoConsoleVariable<float> UUEAutoTrimSystem::CVarTagDisplayTime(
	TEXT("autotrim.TagDisplayTime"),
	1,
	TEXT("Defines the Tag display time in seconds."),
	ECVF_Default);

UUEAutoTrimSystem::UUEAutoTrimSystem()
{
	const ConstructorHelpers::FObjectFinder<UFont> font(TEXT("/Engine/EngineFonts/Roboto"));
	Font = font.Object;
}

void UUEAutoTrimSystem::Initialize(FSubsystemCollectionBase& Collection)
{
	Super::Initialize(Collection);

	const auto drawDebugDelegate = FDebugDrawDelegate::CreateUObject(this, &UUEAutoTrimSystem::Draw);
	DebugDrawHandle = UDebugDrawService::Register(TEXT("GameplayDebug"), drawDebugDelegate);
}

void UUEAutoTrimSystem::Deinitialize()
{
	UDebugDrawService::Unregister(DebugDrawHandle);
	DebugDrawHandle.Reset();

	Super::Deinitialize();
}

void UUEAutoTrimSystem::Start(const FString& InTagName)
{
	if (!ensureAlways(!IsBusy()))
	{
		return;
	}

	Mode = EMode::Start;
	ElapsedTime = 0;
	TagName = InTagName;
	DisplayText = FText::FromString(FString::Printf(TEXT("AutoTrim_Start:%s"), *TagName));
}

void UUEAutoTrimSystem::End()
{
	if (!ensureAlways(!IsBusy()))
	{
		return;
	}

	Mode = EMode::End;
	ElapsedTime = 0;
	DisplayText = FText::FromString(FString::Printf(TEXT("AutoTrim_End:%s"), *TagName));
}

bool UUEAutoTrimSystem::IsBusy() const
{
	return Mode != EMode::None;
}

void UUEAutoTrimSystem::SetTextOffset(const FVector2D& InOffset)
{
	TextOffset = InOffset;
}

void UUEAutoTrimSystem::SetTextColor(const FLinearColor& InColor)
{
	TextColor = InColor;
}

void UUEAutoTrimSystem::SetBackgroundColor(const FLinearColor& InColor)
{
	BackgroundColor = InColor;
}

void UUEAutoTrimSystem::SetBoxSize(const FVector2D& InSize)
{
	BoxSize = InSize;
}

void UUEAutoTrimSystem::SetBoxPosition(const FVector2D& InPosition)
{
	BoxPosition = InPosition;
}


TStatId UUEAutoTrimSystem::GetStatId() const
{
	RETURN_QUICK_DECLARE_CYCLE_STAT(UUEAutoTrimSystem, STATGROUP_Tickables);
}

ETickableTickType UUEAutoTrimSystem::GetTickableTickType() const
{
	return IsTemplate() ? ETickableTickType::Never : ETickableTickType::Always;
}

void UUEAutoTrimSystem::Tick(float DeltaTime)
{
	if (!IsBusy())
	{
		return;
	}

	ElapsedTime += DeltaTime;
	if (ElapsedTime >= CVarTagDisplayTime.GetValueOnAnyThread())
	{
		Mode = EMode::None;
	}
}

void UUEAutoTrimSystem::Draw(UCanvas* InCanvas, APlayerController* InPC)
{
	if (!IsBusy())
	{
		return;
	}

	const float BoxThickness = BoxSize.Y;
	const FVector2D BoxThicknessHalf(BoxThickness / 2, BoxThickness / 2);

	const FVector2D BoxStart(BoxPosition + BoxThicknessHalf);
	InCanvas->K2_DrawBox(BoxStart, FVector2D(BoxSize.X - BoxThickness, 1), BoxThickness, BackgroundColor);
	
	const FVector2D TextStart = BoxPosition + TextOffset;
	FCanvasTextItem TextItem(TextStart, DisplayText, Font, TextColor);
	InCanvas->DrawItem(TextItem);
}
